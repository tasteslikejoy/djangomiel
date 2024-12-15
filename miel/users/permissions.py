from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class IsSuperAdministrator(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            user = request.user
            if not user.is_superadmin:
                raise PermissionDenied("Данный функционал доступен только для Супер Администратора.")
            return True


class IsAdministrator(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            user = request.user
            if not user.is_admin:
                raise PermissionDenied("Данный функционал доступен только для Администраторов.")
            return True


class IsSuperviser(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            user = request.user
            if not all([user.is_superadmin, user.is_admin]):
                return True
            else:
                raise PermissionDenied("Данный функционал доступен только для Руководителей")
