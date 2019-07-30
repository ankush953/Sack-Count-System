from django.contrib import admin
from django.urls import path, include
from .views import home, query


urlpatterns = [
    path('',home,name='home'),
    path('query/',query,name='query')
    
]
