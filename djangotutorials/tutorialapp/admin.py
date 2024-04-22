from django.contrib import admin
from tutorialapp.models import *
from .forms import *
from django.contrib import message

# Register your models here.



admin.site.register(Student),
admin.site.register(Teacher),
admin.site.register(studentform),
admin.site.register(teacherform),



