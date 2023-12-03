from django.contrib.auth.models import User
from django.db import models


class Cource(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description_short = models.CharField(max_length=100, verbose_name='Описание Короткое', default='', null=True, blank=True)
    description_long = models.TextField(verbose_name='Описание Длиннок', default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    image = models.ImageField(upload_to=f'post/%Y/%m/%d', verbose_name='Фото для превью', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cources'
        ordering = ['created_at']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'



class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    description_short = models.CharField(max_length=100, verbose_name='Описание Короткое', default='', null=True, blank=True)
    description_long = models.TextField(verbose_name='Описание Длинное', default='', null=True, blank=True)
    order = models.PositiveIntegerField(default=1, verbose_name='Порядок отображения')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    image = models.ImageField(upload_to=f'post/%Y/%m/%d', verbose_name='Фото для превью', null=True, blank=True)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE, related_name='lessons')
    quiz_link = models.CharField(max_length=250, verbose_name='Ссылка на опрос', default='', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'lessons'
        ordering = ['order', 'created_at']
        verbose_name = 'Модуль курса'
        verbose_name_plural = 'Модули курса'



class Quiz(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    cource = models.OneToOneField(Cource, on_delete=models.CASCADE, related_name='quiz')
    rules = models.TextField(default='', null=True, blank=True, verbose_name="Правила")
    def __str__(self):
        return self.cource.title

    class Meta:
        db_table = 'quizes'
        ordering = ['created_at']
        verbose_name = 'Тест с вопросами'
        verbose_name_plural = 'Тесты с вопросами'






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
        ordering = ['order', 'created_at']
        verbose_name = 'Видеоурок'
        verbose_name_plural = 'Видеоуроки'






class Question(models.Model):
    name = models.CharField(max_length=250, verbose_name="Вопрос")
    link = models.CharField(max_length=250, verbose_name='Ссылка на видео')
    comment = models.TextField(default='')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    order = models.PositiveIntegerField(default=1, verbose_name='Порядок отображения')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    is_active = models.BooleanField(default=True, verbose_name='Активное')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'questions'
        ordering = ['order', 'created_at']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', editable=True)
    order = models.PositiveIntegerField(default=1, verbose_name='Порядок отображения')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    name = models.CharField(max_length=250, verbose_name="Вариант ответа")
    is_right = models.BooleanField(default=True, verbose_name='Верный или нет')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'answers'
        ordering = ['order', 'created_at']
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Вариант ответа'