from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import not_blocked
from .models import Lesson

@login_required
@not_blocked
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

@login_required
@not_blocked
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'lessons': lessons})