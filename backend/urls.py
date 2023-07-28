from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('game_statistics.urls')),
]
