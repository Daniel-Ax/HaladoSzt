# WebshopApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SellNotesForm
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
def sell_notes(request):
    if request.method == 'POST':
        form = SellNotesForm(request.POST, request.FILES)
        if form.is_valid():
            # Menti az adatokat az adatbázisba
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('index_loged_in')
    else:
        form = SellNotesForm()
    return render(request, 'sell_notes.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
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

@login_required
def index_loged_in(request):
    products = Product.objects.all()
    return render(request, 'index_loged_in.html', {'products': products})

def logout_view(request):
    logout(request)
    return redirect('index')