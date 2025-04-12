from django.shortcuts import render, redirect, get_object_or_404
from .models import Card, Lesson
from .forms import CardForm, LessonForm

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'my_app/lesson_list.html', {'lessons': lessons})

def card_list(request, lesson_id=None):
    if lesson_id:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        cards = lesson.cards.all()
    else:
        cards = Card.objects.all()
    return render(request, 'my_app/card_list.html', {'cards': cards})

def card_add(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'my_app/card_add.html', {'form': form})

def card_study(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    cards = lesson.cards.all()
    return render(request, 'my_app/card_study.html', {'cards': cards, 'lesson': lesson})
# Create your views here.
