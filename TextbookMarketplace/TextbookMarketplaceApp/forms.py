# YourAppName/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Product


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User  # Ha a User modellt használod
        fields = ['username', 'email', 'password1', 'password2']


class SellNotesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['institution', 'subject', 'description', 'price', 'file']

    file = forms.FileField()
