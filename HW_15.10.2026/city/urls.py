from django.urls import path

from . import views

app_name = 'city'

urlpatterns = [
    # #1 Основні розділи
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts'),
    # #2 Розділ «Історія» з підрозділами
    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
]
