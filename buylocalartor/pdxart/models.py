from django.db import models
from django.contrib.auth.models import User, UserManager

class Medium(models.Model):
    class Meta:
        verbose_name_plural = "Media"

    material = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return str(self.material)

class Address(models.Model):
    state = models.CharField(max_length=128, default='Oregon')
    street_address = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    def __unicode__(self):
        return str(self.street_address)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    LinkedIn = models.URLField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    address = models.OneToOneField(Address, blank=True, null=True)
    def __unicode__(self):
        return str(self.user)

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    medium = models.ForeignKey(Medium)
    owner = models.ForeignKey(UserProfile)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=500)
    time_sold = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(null=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return str(self.name)