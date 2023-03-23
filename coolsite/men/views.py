from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

# ******************************************************************
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная свзяь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

def home(request):
    posts = Men.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'men/index.html', context = context)
# ******************************************************************

def about(request):
    return render(request, 'men/about.html', {'menu':menu, 'title': 'О сайте'})



# def index(request):
#     return HttpResponse(f'Раздел')


# def person(request, number):
#     return HttpResponse(f'<h1>Вы попали на раздел {number}</h1>')
#
# def archive(request, year):
#     if int(year) > 2023:
#         # raise Http404() #Вызывает ошибку страница не найдена
#         # return redirect('/') #Возвращает на ту страничку, которую указываете
#         # return redirect('/men', permanent=True) #Может использоваться временно
#         return redirect('home')
#     return HttpResponse(f'<h1>Архив года:</h1><p1>{year}</p1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1> Страница не найдена </h1>')
