from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('about/', about, name = 'about'),#http://127.0.0.1:8000/about
    path('', home, name = 'home'),#http://127.0.0.1:8000/
    path('add_page/', add_page, name = 'add_page'),
    path('login/', login, name = 'login'),
    path('contact/', contact, name = 'contact'),
    path('post/<int:post_id>/', show_post, name = 'post'),
    path('category/<int:cat_id>/', show_category, name = 'category')
    # path('nikita/<int:number>/', person), #http://127.0.0.1:8000/men/nikita/2
                                            #внутри стрелок можно использовать различные типы данных:
                                            #str int slug uuid path
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #http://127.0.0.1:8000/men/archive/2022
]

