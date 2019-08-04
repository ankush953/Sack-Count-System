from django.contrib import admin
from django.urls import path, include
from trucks.views import showtruck

urlpatterns = [
    path('',showtruck,name='truck')
    
]
