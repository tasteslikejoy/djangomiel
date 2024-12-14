from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'contact_link', 'is_active',
                    'is_staff', 'is_admin', 'is_superadmin',)
    search_fields = ('email', 'first_name', 'last_name', 'contact_link',)
    list_filter = ('is_staff', 'is_admin', 'is_superadmin')
