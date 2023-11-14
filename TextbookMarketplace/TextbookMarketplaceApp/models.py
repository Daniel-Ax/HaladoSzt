from django.db import models

class YourModel(models.Model):
    # Your fields go here
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
