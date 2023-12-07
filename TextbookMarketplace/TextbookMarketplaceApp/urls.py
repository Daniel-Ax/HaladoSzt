# TextbookMarketplaceApp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    IndexView,
    CheckoutView,
    SellNotesView,
    LoginView,
    RegistrationView,
    IndexLoggedInView,
    LogoutView,
    ProductDetailView,
    AddToCartView,
    ViewCartView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('sell_notes/', SellNotesView.as_view(), name='sell_notes'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('index_logged_in/', IndexLoggedInView.as_view(), name='index_logged_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('view_cart/', ViewCartView.as_view(), name='view_cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
