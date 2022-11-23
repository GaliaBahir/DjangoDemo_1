from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='author')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
