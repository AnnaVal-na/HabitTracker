from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """ Кастомный менеджер для модели User без использования username """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Создает и сохраняет пользователя с заданным email и паролем """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ Создает обычного пользователя """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ Создает суперпользователя """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ Кастомная модель пользователя с email в качестве идентификатора """
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = 'email'  # Используем email для аутентификации
    REQUIRED_FIELDS = []  # Список полей, обязательных при создании суперпользователя

    objects = UserManager()  # Подключаем наш кастомный менеджер

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
