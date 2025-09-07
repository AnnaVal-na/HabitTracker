from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Habit

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
