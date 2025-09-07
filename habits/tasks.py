from celery import shared_task
from django.utils import timezone
from .models import Habit
from .services import send_telegram_message


@shared_task
def send_habit_reminders():
    """Отправляет напоминания о привычках"""
    now = timezone.now()
    current_time = now.time()

    # Находим привычки для текущего времени
    habits = Habit.objects.filter(time__hour=current_time.hour,
                                  time__minute=current_time.minute)

    for habit in habits:
        if habit.user.telegramchat:
            message = f"⏰ Напоминание: {habit.action} в {habit.time} в {habit.place}"
            send_telegram_message(habit.user.telegramchat.chat_id, message)
