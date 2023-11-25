from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=False)
    file = models.FileField(upload_to='files/', null=False)
    institution = models.CharField(max_length=255, null=False)
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
