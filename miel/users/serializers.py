from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


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
        # fields = tuple(User.REQUIRED_FIELDS) + (
        #     settings.LOGIN_FIELD,
        #     settings.USER_ID_FIELD,
        #     "password",
        # )
        #
