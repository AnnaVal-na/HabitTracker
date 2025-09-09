from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Кастомный сериализатор для добавления полей в JWT-токен (опционально) """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Добавляем свои поля в токен
        token['email'] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для регистрации и отображения пользователя """
    # Делаем поле password write_only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        # Дополнительные настройки (опционально):
        extra_kwargs = {
            'password': {'write_only': True},
        }


    def create(self, validated_data):
        """ Переопределяем метод create для хеширования пароля """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

