
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers , permissions
from showcase.views import CandidateCardViewSet, CandidateCardViewSetDirektor




router = routers.DefaultRouter()
router.register(r'candidat_list', CandidateCardViewSet, basename='candidat_list')
router.register(r'candidatdirektor_list', CandidateCardViewSetDirektor, basename='candidatdirektor_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
