from django import forms
from django.forms import ModelForm
from . models import *
class taskForm(forms.ModelForm):
    title= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add New Task'}))
    class Meta:
        model= task
        fields= '__all__'