import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from habits.models import TelegramChat
from users.models import User


class Command(BaseCommand):
    help = 'Получить chat_id из Telegram бота'

    def handle(self, *args, **options):
        bot_token = settings.TELEGRAM_BOT_TOKEN

        if not bot_token:
            self.stdout.write(self.style.ERROR('Ошибка: TELEGRAM_BOT_TOKEN не настроен в .env!'))
            return

        url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

        try:
            response = requests.get(url)
            data = response.json()

            if not data['ok']:
                self.stdout.write(self.style.ERROR('Ошибка от Telegram API'))
                return

            for update in data['result']:
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    username = update['message']['chat'].get('username', 'неизвестно')
                    first_name = update['message']['chat'].get('first_name', '')

                    self.stdout.write(self.style.SUCCESS(
                        f"Найден chat_id: {chat_id} для пользователя: {first_name} (@{username})"
                    ))

                    # Сохраняем в базу (привязываем к первому пользователю для примера)
                    user = User.objects.first()
                    if user:
                        TelegramChat.objects.get_or_create(
                            user=user,
                            defaults={'chat_id': chat_id}
                        )
                        self.stdout.write(self.style.SUCCESS(f'Chat_id сохранен для пользователя {user.email}'))

            if not data['result']:
                self.stdout.write(self.style.WARNING('Новых сообщений нет. Напиши боту в Telegram сначала!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: {e}'))
