# YourAppName/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Ha a User modellt használod
        fields = ['username', 'email', 'password1', 'password2']


class SellNotesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['institution', 'name', 'subject', 'description', 'price', 'category', 'is_available', 'image']

    image = forms.FileField()
    category = forms.CharField(max_length=255)
    is_available = forms.BooleanField(required=False, initial=True)
