from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    """ ViewSet для привычек """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # Только аутентифицированные пользователи и только свои привычки


    def get_queryset(self):
        # Пользователь видит только свои привычки
        return Habit.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        # Автоматически привязываем привычку к текущему пользователю
        serializer.save(user=self.request.user)
        