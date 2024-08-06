from django.urls import path
from . import views


urlpatterns = [
    path('',views.Fibonacci_Gen,name='Fibonacci_Gen'),
    path('home',views.Fibonacci_Gen,name='home')
]