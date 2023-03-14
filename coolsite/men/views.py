from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.


def home(request):
    return HttpResponse(f'<h1>Главная страница</h1>')

def index(request):
    return HttpResponse(f'Раздел')

def person(request, number):
    return HttpResponse(f'<h1>Вы попали на раздел {number}</h1>')

def archive(request, year):
    if int(year) > 2023:
        # raise Http404() #Вызывает ошибку страница не найдена
        # return redirect('/') #Возвращает на ту страничку, которую указываете
        # return redirect('/men', permanent=True) #Может использоваться временно
        return redirect('home')
    return HttpResponse(f'<h1>Архив года:</h1><p1>{year}</p1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1> Страница не найдена </h1>')
