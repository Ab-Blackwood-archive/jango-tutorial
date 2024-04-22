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

def Teacherform(request):
    context = {}
    if request.method == "POST":
        form = teacherform(request.POST)
        if form.is_valid():
            context = ""
            for name, value in form.cleaned_data.items():
                print("{}: ({} {}".format (name,type(value), value))
        requests = form.save(commit=False)

        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lasttname']
        middlename = form.cleaned_data['middlename']
        subject = form.cleaned_data['subject']
        roomnumber = form.cleaned_data['roomnumber']
        requests.save()
    else:
        form = Teacherform()
    return render(request, "teacherform.html",{"method": request.method, "form":form})

def Studentform(request):
    context = {}
    if request.method == "POST":
        form = Studentform(request.POST)
        if form.is_valid():
            context = ""
            for name, value in form.cleaned_data.items():
                print("{}: ({} {}".format (name,type(value), value))
        requests = form.save(commit=False)

        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lasttname']
        middlename = form.cleaned_data['middlename']
        grade = form.cleaned_data['grade']
        requests.save()

        messages.success(request,"New Student added successfully! ")
    else:
        form = Studentform()
    return render(request, "studentform.html",{"method": request.method, "form":form})







