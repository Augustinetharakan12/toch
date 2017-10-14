from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="osat"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^a_registration/$', views.a_registration, name='a_registration'),
    url(r'^h_registration/$', views.h_registration, name='h_registration'),
    url(r'^e_registration/$', views.e_registration, name='e_registration'),
    url(r'^c_us/$', views.c_us, name='c_us'),
    url(r'^notifications/$', views.notific, name='notific'),


]
