from django.urls import path
from . import views

app_name = 'test'
urlpatterns = [
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
    path('c/', views.c, name='c'),
]
