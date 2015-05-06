from django.db import models
from django.contrib.auth.models import User, UserManager

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


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


class Profilepic(models.Model):
    avatar = models.ImageField(upload_to='/media/profile_images')
    avatar_thumbnail = ImageSpecField(source='/media/profile_images',
                                      processors=[ResizeToFill(100, 50)],
                                      format='PNG',
                                      options={'quality': 60})


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    address = models.OneToOneField(Address, blank=True, null=True)
    # gender = models.CharField(max_length=1, blank=True)
    picture = models.ImageField(upload_to='/media/profile_images', blank=True)

    # avatar = models.OneToOneField(Profilepic, blank=True, null=True)

    # def avatar_image(self):
    #     if has image:
    #         return ('/media/profile_images/' + self + '.png')
    #     else:
    #         return ('/media/profile_images/default_profile_pic.jpg'')

    def __unicode__(self):
        return str(self.user.username)


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField(default=0)
    medium = models.ForeignKey(Medium, null=True)
    owner = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=500)
    time_sold = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(null=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return str(self.name)