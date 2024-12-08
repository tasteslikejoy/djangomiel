from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.decorators import api_view, permission_classes

from .permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


# Create your views here.


class TestApiView(APIView):

    permission_classes = [IsSuperviser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data,
        })
