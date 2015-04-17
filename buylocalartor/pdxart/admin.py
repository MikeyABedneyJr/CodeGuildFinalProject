from django.contrib import admin
from pdxart.models import Medium, UserProfile, Product
from imagekit.admin import AdminThumbnail
from .models import Photo

# class MediumAdmin(admin.ModelAdmin):
#     list_display = ('material')
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Medium)
admin.site.register(UserProfile)
admin.site.register(Product)