from socket import fromshare
from django import forms
from .models import*

class studentform(forms.Modelform):
    class Meta:
        model = Student
        fields = ["firstname","lastname", "middlename","grade"]

class teacherform(forms.Modelform):
    class Meta:
        model = Teacher
        fields = ["firstname","lastname", "middlename","roomnum","subject"]