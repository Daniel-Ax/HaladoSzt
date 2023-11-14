from django.urls import path
from TextbookMarketplaceApp.views import index, home, register  # Ensure correct imports
# TextbookMarketplaceApp/urls.py
from TextbookMarketplaceApp.views import register  # Correct the import


urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    # Other URL patterns go here
]
