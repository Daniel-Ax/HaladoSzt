# WebshopApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def checkout(request):
    return render(request, 'checkout.html')

def sell_notes(request):
    return render(request, 'sell_notes.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Felhasználó sikeresen regisztrálva, átirányítás az új nézetbe vagy oldalra.
            return redirect('login')  # Cseréld le az 'index' azonosítót az általad kívántra.
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
