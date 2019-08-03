from django.contrib import admin
from django.urls import path, include
from .views import home, query, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('query/', query, name='query'),
    path('about/',about,name='about')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
