from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('',views.home, name='home'),
    path('students/',views.Students, name='students'),
    path('teachers',views.Teachers, name='teachers'),
]