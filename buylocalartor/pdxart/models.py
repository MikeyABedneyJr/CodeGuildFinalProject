from django.db import models
from django.contrib.auth.models import User, UserManager

class Medium(models.Model):
    material = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.material

#TODO: Ask for easier model
class Address(models.Model):
    state = models.CharField('Oregon')
    house_number = models.IntegerField(blank=True)
    street_name = models.CharField(blank=True)
    apartment_or_pobox = models.CharField(blank=True)
    compass = models.CharField(blank=True)

class UserProfile(User):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    LinkedIn = models.URLField(blank=True)
    bio = models.TextField(max_length=500)
    address = models.ForeignKey(Address)


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    medium = models.ForeignKey(Medium)
    owner = models.ForeignKey(UserProfile)
    description = models.TextField(max_length=500)
    time_sold = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name




