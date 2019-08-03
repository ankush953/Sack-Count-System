from django.contrib import admin
from django.urls import path, include
# from .views import Home
from django.conf import settings
from django.conf.urls.static import static

from companies.views import company_registration

urlpatterns = [
    path('register/', company_registration, name='companyregistration')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
