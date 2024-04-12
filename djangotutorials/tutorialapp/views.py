from django.shortcuts import render
from .models import *
# Create your views here.

def base(request):
    context ={

    }

    return render(request, 'base.html', context)

def home(request):
    context ={

    }

    return render(request, 'home.html', context)

def Students(request):
    students = Student.objects.all()# get all regords and saves student to list
    context={
        'students':students, #exports students list to template(webpage)

    }

    return render(request, 'students.html', context)

def Teachers(request):
    teachers = Teacher.objects.all()# get all regords and saves student to list
    context={
        'teachers':teachers, #exports students list to template(webpage)

    }

    return render(request, 'teachers.html', context)


