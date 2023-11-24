from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return HttpResponse("Hello, this is your app's index view.")

def home(request):
    return HttpResponse("Welcome to the Textbook Marketplace!")

# TextbookMarketplaceApp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration_form.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

def login_view(request):
    return CustomLoginView.as_view()(request)

# views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


