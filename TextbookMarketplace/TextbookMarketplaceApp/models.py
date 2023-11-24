from django.db import models

class YourModel(models.Model):
    # Your fields go here
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name


