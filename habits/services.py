import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    """
    Отправляет сообщение в Telegram через бота
    :param chat_id: ID чата куда отправлять
    :param message: Текст сообщения
    :return: True если успешно, False если ошибка
    """
    bot_token = settings.TELEGRAM_BOT_TOKEN

    if not bot_token:
        print("Ошибка: TELEGRAM_BOT_TOKEN не настроен!")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")
        return False
