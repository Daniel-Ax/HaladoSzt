# TextbookMarketplaceApp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    IndexView,
    SellNotesView,
    LoginView,
    RegistrationView,
    IndexLoggedInView,
    LogoutView,
    ProductDetailView,
    DeleteProductView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sell_notes/', SellNotesView.as_view(), name='sell_notes'),
    path('product/delete/<int:product_id>/', DeleteProductView.as_view(), name='delete_product'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('index_logged_in/', IndexLoggedInView.as_view(), name='index_logged_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
