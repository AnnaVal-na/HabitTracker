from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """ Разрешение на доступ только к своим привычкам """
    def has_object_permission(self, request, view, obj):
        # Проверяем, что пользователь является владельцем привычки
        return obj.user == request.user
    