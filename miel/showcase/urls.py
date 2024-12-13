from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'candidat', views.CandidateCardViewSet)
router.register(r'candidatdirektor', views.CandidateCardViewSetDirektor)

urlpatterns = [
    path('', include(router.urls)),

]