from rest_framework import generics, viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    """ ViewSet для привычек """
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """Эндпоинт для публичных привычек"""
    serializer_class = HabitSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Habit.objects.filter(is_public=True)
