from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/', views.base, name='base'),
    path('',views.home, name='home'),
    path('students/',views.Students, name='students'),
    path('teachers/',views.Teachers, name='teachers'),
    path('teacherform/',views.teacherform, name='teacherform'),
    path('studentform/', views.studentform, name='studentform'),
]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)