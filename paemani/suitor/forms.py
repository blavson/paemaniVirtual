from django import forms
from .choices import *
from .models import Suitor,Aprnc
from django.forms import ModelForm

class SuitorForm(ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Lastname', max_length=100)
    dob = forms.DateField()
    email = forms.EmailField()
    gender=forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = Suitor
        fields = ['name', 'last_name', 'gender', 'dob', 'email']

class AprncForm(ModelForm):
    hair_color = forms.ChoiceField(choices=HAIR_COLOR_CHOICES)
    ethnicity = forms.ChoiceField(choices=ETHNICITY_CHOICES)

    class Meta:
        model = Aprnc
        fields =['ethnicity','hair_color', 'height', 'weight']
