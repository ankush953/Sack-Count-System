from django.contrib import admin
from django.urls import path, include
from .views import new_user, update_profile, logout_view, login_view, update_profile, view_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('newuser/', new_user, name='newuser'),
    path('profile/<str:username>', view_profile, name='profile'),
    path('updateprofile/<str:username>/', update_profile, name='updateprofile'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


CRISPY_TEMPLATE_PACK = 'bootstrap4'
