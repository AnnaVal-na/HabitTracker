from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Habit
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )

    def test_habit_creation(self):
        habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="12:00:00",
            action="Читать книгу",
            duration=120,
            is_public=True
        )
        self.assertEqual(habit.action, "Читать книгу")


class HabitAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('habit-list')
        data = {
            'place': 'Дом',
            'time': '12:00:00',
            'action': 'Читать книгу',
            'duration': 120,
            'is_public': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
