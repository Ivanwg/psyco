from django.contrib.auth.models import User
from django.db import models


class Cource(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    image = models.ImageField(upload_to=f'post/%Y/%m/%d', verbose_name='Фото для превью', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cources'
        ordering = ['-created_at']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    # def get_absolute_url(self):
    #     return reverse('news_detail', kwargs={'pk': self.pk})

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    image = models.ImageField(upload_to=f'post/%Y/%m/%d', verbose_name='Фото для превью', null=True, blank=True)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'lessons'
        ordering = ['-created_at']
        verbose_name = 'Модуль курса'
        verbose_name_plural = 'Модули курса'

    # def get_absolute_url(self):
    #     return reverse('news_detail', kwargs={'pk': self.pk})

class Quiz(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quiz')

    def __str__(self):
        return self.lesson.title

    class Meta:
        db_table = 'quizes'
        ordering = ['-created_at']
        verbose_name = 'Тест с вопросами'
        verbose_name_plural = 'Тесты с вопросами'

    # def get_absolute_url(self):
    #     return reverse('news_detail', kwargs={'pk': self.pk})




class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    order = models.PositiveIntegerField(default=1, verbose_name='Порядок отображения')
    link = models.CharField(max_length=250, verbose_name='Ссылка на видео')
    description = models.CharField(max_length=250, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    image = models.ImageField(upload_to=f'post/%Y/%m/%d', verbose_name='Фото для превью', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'videos'
        ordering = ['-created_at']
        verbose_name = 'Видеоурок'
        verbose_name_plural = 'Видеоуроки'

    # def get_absolute_url(self):
    #     return reverse('news_detail', kwargs={'pk': self.pk})




# class Image(models.Model):
#     photo = models.ImageField(upload_to=f'post/%Y/%m/%d')
#     item = models.ForeignKey(Cource, on_delete=models.PROTECT, related_name='images', unique=False)
#
#     class Meta:
#         db_table = 'images'
#         verbose_name = 'images'
#         verbose_name_plural = 'images'


