from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index), #http://127.0.0.1:8000/
    path('nikita/<int:number>/', person), #http://127.0.0.1:8000/men/nikita/2
                                            #внутри стрелок можно использовать различные типы данных:
                                            #str int slug uuid path
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #http://127.0.0.1:8000/men/archive/2022
]
