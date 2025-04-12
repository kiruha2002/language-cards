from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/<int:lesson_id>/', views.card_list, name='card_list_lesson'),
    path('cards/add/', views.card_add, name='card_add'),
    path('study/<int:lesson_id>/', views.card_study, name='card_study'),
]