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
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'first_name',
            'last_name',
            'middle_name',
            'contact_link',
            'role',
        )

    def get_role(self, obj):
        role = None
        if obj.is_staff:
            role = 'БигБосс'
        elif not all([obj.is_superadmin, obj.is_admin]):
            role = 'Руководитель'
        elif obj.is_superadmin:
            role = 'СуперАдминистратор'
        elif obj.is_admin:
            role = 'Администратор'

        return role
