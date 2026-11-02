from django.urls import path

from . import views

app_name = 'keepsimple'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/single/', views.single, name='single'),
    path('page/', views.page, name='page'),
    path('archives/', views.archives, name='archives'),
    path('demo/', views.demo, name='demo'),
]
