from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


# Create your views here.


# class CreateAdminUserViewset(UserViewSet):
class CreateAdminUserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsSuperAdministrator]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    http_method_names = ['post']

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(*args, **kwargs, is_admin=True)
