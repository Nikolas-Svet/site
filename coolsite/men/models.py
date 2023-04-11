from django.db import models
from django.urls import reverse

class Men(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    # cat ссылается на класс Category

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    # Функция возвращает url

    class Meta: #Класс, используемый для адми-панели
        verbose_name = "Мужчины" #Название вкладки в админ-панели
        verbose_name_plural = "Мужчины" #Название вкладки в админ-панели
        ordering = ['time_create', 'title'] #Сортировка данных

# Дополнительная таблица, разделяющая класс Men на категории
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

