
from django.contrib import admin
from .models import Lesson, Card

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation', 'lesson', 'created_at')
