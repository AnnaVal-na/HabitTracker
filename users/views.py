from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    """ View для регистрации нового пользователя """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Разрешаем доступ без аутентификации
