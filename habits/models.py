from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

NULLABLE = {'blank': True, 'null': True}

class Habit(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=255, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='связанная привычка')
    frequency = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='daily', verbose_name='периодичность')
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='вознаграждение')
    duration = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)], verbose_name='время на выполнение (секунды)')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')


    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
