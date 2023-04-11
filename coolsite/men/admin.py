from django.contrib import admin

from .models import *

class MenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(Men, MenAdmin) #Создает вкладку Men в админ-панели

# Register your models here.
