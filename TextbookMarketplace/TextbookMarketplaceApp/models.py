from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class YourModel(models.Model):
    # Your fields go here
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=255,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=False)
    file = models.FileField(upload_to='files/',null=False)
    institution = models.CharField(max_length=255,null=False)
    subject = models.CharField(max_length=255,null=False)
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


