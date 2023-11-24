# WebshopApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html')

def checkout(request):
    return render(request, 'checkout.html')

def sell_notes(request):
    return render(request, 'sell_notes.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})