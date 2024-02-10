from django import forms

from .models import MyTodoList


# Create your models here.

class TodoList(forms.Form):
    task = forms.CharField(max_length=80)
    time_interval = forms.CharField(max_length=50)

