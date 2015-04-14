from django.conf.urls import patterns, url
from pdxart import views

urlpatterns = patterns('',
        url(r'^index/', views.index, name='index'),
        url(r'^registration/', views.registration, name='registration'),
        )
