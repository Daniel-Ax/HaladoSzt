# WebshopApp/urls.py

from django.urls import path
from .views import index, checkout, sell_notes, login, registration, index_loged_in, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('checkout/', checkout, name='checkout'),  # Új URL a fizető oldalhoz
    path('sell_notes/', sell_notes, name='sell_notes'), #Új jegyzet hozzáadása
    path('login', login, name='login'), #login view path
    path('registration', registration, name='registration'), #reg view path
    path('index_loged_in', index_loged_in, name='index_loged_in'),
    path('logout/', logout_view, name='logout'),
]