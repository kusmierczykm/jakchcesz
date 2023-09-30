
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='website_index'),
    path('create_recorded_time', views.create_recorded_time, name='create_recorded_time'),

]
