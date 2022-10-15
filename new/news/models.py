from django.db import models


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва кетегорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class News(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='Назва новини')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/%H/%M/%S', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано ?')
    cost = models.FloatField(null=True, verbose_name='Ціна', blank=True)
    we_have = models.BooleanField(default=False, verbose_name='Є в наявності?', blank=True)
    rating = models.FloatField(null=True, verbose_name='Рейтинг', blank=True)
    categores = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at', 'title']




