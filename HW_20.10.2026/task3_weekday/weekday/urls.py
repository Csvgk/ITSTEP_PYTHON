from django.urls import path

from . import views

app_name = 'weekday'

urlpatterns = [
    path('', views.index, name='index'),
]
