from django.contrib import admin
from .models import Lesson, Quiz

class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 0  # Убрано лишнее поле по умолчанию
    fields = ('question', 'option_a', 'option_b', 'option_c', 'correct_answer')
    min_num = 0  # Минимум тестов — 0 (опционально)

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuizInline]
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz)