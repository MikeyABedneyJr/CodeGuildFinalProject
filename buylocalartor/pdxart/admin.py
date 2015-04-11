from django.contrib import admin
from pdxart.models import Medium, UserProfile, Product

# class MediumAdmin(admin.ModelAdmin):
#     list_display = ('material')

admin.site.register(Medium)
admin.site.register(UserProfile)
admin.site.register(Product)