from django.contrib import admin
from videos.models import *


class VideoItemInline(admin.TabularInline):
    model = Video



# class LessonItemInline(admin.TabularInline):
#     model = Lesson
#     inlines = [VideoItemInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'updated_at', 'is_active')
    list_filter = ('is_active', 'updated_at')
    list_editable = ('is_active',)
    # inlines = [LessonItemInline]

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at', 'is_active')
    list_filter = ('is_active', 'updated_at')
    list_editable = ('is_active', 'order')
    search_fields = ('title',)
    # inlines = [LessonItemInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'is_active')
    list_filter = ('is_active', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('title',)
    # inlines = [LessonItemInline]



class CourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'is_active')
    list_filter = ('is_active', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('title',)
    # inlines = [LessonItemInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Cource, CourceAdmin)