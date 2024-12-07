from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.decorators import api_view, permission_classes

from .permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .serializers import UserRegistrationSerializer

User = get_user_model()


# Create your views here.


class TestApiView(APIView):

    permission_classes = [IsSuperviser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)

        user = request.user
        role = None

        if not all([user.is_superadmin, user.is_admin]):
            role = 'Руководитель'
        elif user.is_superadmin:
            role = 'СуперАдминистратор'
        elif user.is_admin:
            role = 'Администратор'

        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data,
            'user_role': role,
        })
