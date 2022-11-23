from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=250,db_index=True)

class Product(models.Model):
    #category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='author')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
