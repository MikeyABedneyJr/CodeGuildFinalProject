from django.conf.urls import patterns, url
from pdxart import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^registration/', views.registration, name='registration'),
        url(r'^updateprofile/', views.update_profile, name='updateprofile'),
        url(r'^profile/', views.profile, name='profile'),
        url(r'^login/$', views.user_login, name='login'),
        )
