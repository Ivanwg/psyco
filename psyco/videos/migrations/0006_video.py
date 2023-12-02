# Generated by Django 3.2 on 2023-11-30 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('link', models.CharField(max_length=250, verbose_name='Ссылка на видео')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активное')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/%Y/%m/%d', verbose_name='Фото для превью')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.lesson')),
            ],
            options={
                'verbose_name': 'Видеоурок',
                'verbose_name_plural': 'Видеоуроки',
                'db_table': 'videos',
                'ordering': ['-created_at'],
            },
        ),
    ]
