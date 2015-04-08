from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
