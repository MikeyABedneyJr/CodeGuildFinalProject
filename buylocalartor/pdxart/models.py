from django.db import models
from django.contrib.auth.models import User, UserManager

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    medium = models.ForeignKey.Medium
    owner = models.ForeignKey.UserProfile
    description = models.TextField(max_length=500)
    time_sold =
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Medium(model.Models):
    material = models.CharField(max_length=128, unique=True)

#class UserProfile(User):
