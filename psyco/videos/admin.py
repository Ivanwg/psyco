from django.contrib import admin
from videos.models import *




class AnswerInline(admin.TabularInline):
    model = Answer

    

class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'order', 'updated_at',)
    list_filter = ('updated_at',)
    list_editable = ('order',)

    inlines = [AnswerInline]


class QuizAdmin(admin.ModelAdmin):
    list_display = ('cource', 'updated_at',)
    list_filter = ('updated_at',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at',)
    list_filter = ('updated_at',)
    list_editable = ('order',)
    search_fields = ('title',)
    # inlines = [LessonItemInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at',)
    list_filter = ('updated_at',)
    list_editable = ('order',)
    search_fields = ('title',)
    # inlines = [LessonItemInline]



class CourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at',)
    list_filter = ('updated_at',)
    search_fields = ('title',)
    # inlines = [LessonItemInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Cource, CourceAdmin)