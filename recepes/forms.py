from django.forms import ModelForm
from django import forms
from .models import Recepes

class RecepesForm(ModelForm):
    class Meta:
        model = Recepes
        fields = '__all__'
        exclude = ['user']
