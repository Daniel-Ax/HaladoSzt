from django.urls import path
from TextbookMarketplaceApp.views import index, home, register, login_view  # Ensure correct imports
# TextbookMarketplaceApp/urls.py
from TextbookMarketplaceApp.views import register  # Correct the import


urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    # Other URL patterns go here
]
