from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError()

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        '''Добавить отправку с паролем на почту пользователю'''

        return user

    '''create admin and superadmin'''

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    class UserRoles(models.TextChoices):
        administrator = 'admin', 'Администратор'
        staff = 'staff', 'БигБосс'
        superviser = 'superviser', 'Руководитель'
        superadmin = 'superadmin', 'СуперАдминистратор'

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    contact_link = models.CharField(max_length=255, null=True, blank=True)
    # is_active = models.BooleanField(default=False)  #TODO нужно для подтверждения по email?
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'middle_name',
    ]

    objects = UserManager()

    def get_role(self):
        role = User.UserRoles.staff
        if self.is_staff:
            role = User.UserRoles.staff
        elif not any([self.is_superadmin, self.is_admin]):
            role = User.UserRoles.superviser
        elif self.is_superadmin:
            role = User.UserRoles.superadmin
        elif self.is_admin:
            role = User.UserRoles.administrator

        return role
