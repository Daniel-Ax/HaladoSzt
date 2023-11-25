# WebshopApp/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Product, Cart, CartItem
from .forms import SellNotesForm, RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout.html'


class SellNotesView(LoginRequiredMixin, View):
    template_name = 'sell_notes.html'
    form_class = SellNotesForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('index_logged_in')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index_logged_in')
        return render(request, self.template_name, {'form': form})


class RegistrationView(View):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_logged_in')
        return render(request, self.template_name, {'form': form})


class IndexLoggedInView(LoginRequiredMixin, TemplateView):
    template_name = 'index_logged_in.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context['product'] = get_object_or_404(Product, pk=pk)
        return context


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        user = request.user
        product = Product.objects.get(pk=product_id)

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        messages.success(request, f"{product.name} added to your cart.")
        return redirect(reverse('index_logged_in'))


class ViewCartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        context['cart_items'] = cart.items.all()
        return context


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class IndexView(BaseView):
    template_name = 'index.html'


class SellNotesView(BaseView):
    template_name = 'sell_notes.html'
