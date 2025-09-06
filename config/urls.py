from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserCreateAPIView
from users.serializers import MyTokenObtainPairSerializer  # Импортируем кастомный сериализатор

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Эндпоинты для JWT-аутентификации
    path('api/token/', TokenObtainPairView.as_view(serializer_class=MyTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Эндпоинт для регистрации
    path('api/users/register/', UserCreateAPIView.as_view(), name='user_register'),
    
    # Сюда позже подключу урлы от приложения habits
    # path('api/', include('habits.urls')),
]
