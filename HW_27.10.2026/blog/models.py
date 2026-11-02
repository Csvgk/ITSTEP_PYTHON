from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


# #1 Модель Tag
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Назва')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Вміст')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    # #1 Зв'язок "багато до багатьох": у поста багато тегів, тег може бути в багатьох постах
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Теги')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Публікація'
        verbose_name_plural = 'Публікації'


# #2 Профіль користувача
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Користувач')
    bio = models.TextField(blank=True, verbose_name='Про себе')
    city = models.CharField(max_length=100, blank=True, verbose_name='Місто')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата народження')

    def __str__(self):
        return f'Профіль {self.user.username}'

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'
