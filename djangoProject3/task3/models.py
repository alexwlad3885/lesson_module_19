from django.db import models


# модель для категории новостей
class Category(models.Model):
    name = models.CharField(max_length=225, verbose_name="Название категории")

    def __str__(self):
        return self.name


# модель для автора
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Автор")

    def __str__(self):
        return self.name


# модель для сайта опубликования новости
class PublicationSite(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сайт")
    publication_date = models.DateTimeField(auto_now=True, verbose_name="Дата опубликования")

    def __str__(self):
        return self.name


# модель для новостей
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title
