from django.forms import ModelForm
from django import forms
from .models import Employee, Lead


class EmployeeForm(ModelForm) :
    class Meta : 
        model = Employee
        fields = '__all__'


class LoginForm(forms.Form) :
    username = forms.CharField(label = 'username', max_length = 100) 
    password = forms.CharField(label = 'password', max_length = 20)


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'project', 'segment', 'submitted_by', 'submitted_to']

