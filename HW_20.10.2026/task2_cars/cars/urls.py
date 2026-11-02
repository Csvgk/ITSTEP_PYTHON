from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('toyota/', views.toyota, name='toyota'),
    path('honda/', views.honda, name='honda'),
    path('renault/', views.renault, name='renault'),
]
