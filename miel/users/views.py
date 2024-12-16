from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .serializers import UserRegistrationSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

User = get_user_model()


# Create your views here.


# class CreateAdminUserViewset(UserViewSet):
@extend_schema(tags=['API для работы с пользователями'])
@extend_schema_view(create=extend_schema(summary='API для создания пользователя-администратора.'))
class CreateAdminUserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsSuperAdministrator]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    http_method_names = ['post']

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(*args, **kwargs, is_admin=True)
