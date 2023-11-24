# WebshopApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def checkout(request):
    return render(request, 'checkout.html')

def sell_notes(request):
    return render(request, 'sell_notes.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index_loged_in')  # Cseréld le az 'index' azonosítót az általad kívántra.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})