from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return HttpResponse("Hello, this is your app's index view.")

def home(request):
    return HttpResponse("Welcome to the Textbook Marketplace!")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page or any other desired page
    else:
        form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})
