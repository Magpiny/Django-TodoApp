from django import forms
from django.forms import ModelForm, fields

from .models import TodoForm

class MyForm(ModelForm):
    task  = forms.CharField(label='Task')
    mdate = forms.DateField(label='Date')
    mtime = forms.TimeField(label='Time')
    deadline = forms.DateTimeField(label='Deadline')

    class Meta:
        model = TodoForm
        fields = ['task', 'mdate', 'mtime', 'deadline']
