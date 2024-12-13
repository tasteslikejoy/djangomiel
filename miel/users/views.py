from django.contrib.auth import get_user_model
from django.shortcuts import render
from djoser.views import UserViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.generics import CreateAPIView

from .permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


# Create your views here.


class CreateAdminUserViewset(UserViewSet):
    permission_classes = [IsAdminUser | IsSuperAdministrator]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(*args, **kwargs, is_admin=True)
