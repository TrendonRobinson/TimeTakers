from django.contrib import admin
from .models import Bow, Purchase, TimeStatistics

admin.site.register(Bow)
admin.site.register(Purchase)
admin.site.register(TimeStatistics)
