from django.contrib import admin
from pdxart.models import Medium, UserProfile

# class MediumAdmin(admin.ModelAdmin):
#     list_display = ('material')

admin.site.register(Medium)
admin.site.register(UserProfile)