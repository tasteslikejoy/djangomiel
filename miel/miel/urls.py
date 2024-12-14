from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('showcase.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
]
