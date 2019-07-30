from django.contrib import admin
from sacks.models import Sack, SackLoading, SackUnloading
# Register your models here.
admin.site.register(Sack)
admin.site.register(SackUnloading)
admin.site.register(SackLoading)