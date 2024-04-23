from socket import fromshare
from django import forms
from .models import*

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["firstname","lastname", "middlename","grade"]

class Teacherform(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["firstname","lastname", "middlename","roomnum","subject"]