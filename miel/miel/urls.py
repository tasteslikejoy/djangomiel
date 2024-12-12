
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers , permissions
from showcase.views import CandidateCardViewSet




router = routers.DefaultRouter()
router.register(r'candidat_list', CandidateCardViewSet, basename='candidat_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
