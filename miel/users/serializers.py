from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers


User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = (
            'email',
            'phone',
            'first_name',
            'last_name',
            'middle_name',
            'contact_link',
            'password',
        )


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='get_role')

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone',
            'first_name',
            'last_name',
            'middle_name',
            'contact_link',
            'role',
        )
