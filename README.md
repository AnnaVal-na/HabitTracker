# HabitTracker - Трекер полезных привычек

[![Django](https://img.shields.io/badge/Django-5.2.3-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-blue)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.13-yellow)](https://www.python.org/)
[![Coverage](https://img.shields.io/badge/coverage-80%25-success)](https://github.com/AnnaVal-na/HabitTracker)

Backend-часть SPA веб-приложения для отслеживания и управления персональными привычками с напоминаниями в Telegram.

## Основные возможности

- CRUD операции с привычками
- JWT-аутентификация и регистрация пользователей
- Telegram-интеграция для напоминаний
- Периодические задачи через Celery
- CORS-настройки для фронтенда
- Публичные привычки для общего доступа
- Валидация данных согласно бизнес-правилам

## Архитектура

- Backend: Django 5.2 + Django REST Framework
- Аутентификация: JWT токены
- Брокер задач: Redis + Celery
- Уведомления: Telegram Bot API
- База данных: SQLite (разработка) / PostgreSQL (продакшен)

##  Быстрый старт

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Настройка переменных окружения

Создайте файл .env в корне проекта:

```dotenv
SECRET_KEY=your-secret-key
DEBUG=True
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

### Миграции базы данных

```bash
python manage.py migrate
```

### Запуск сервера

```bash
python manage.py runserver
```

### Запуск Celery worker

```bash
celery -A config worker --loglevel=info
```

### Запуск Celery beat

```bash
celery -A config beat --loglevel=info
```

### API Endpoints

#### Аутентификация
```text
POST /api/token/ - Получение JWT токена
POST /api/token/refresh/ - Обновление токена
POST /api/users/register/ - Регистрация пользователя
```

#### Привычки
```text
GET /api/habits/ - Список привычек пользователя
GET /api/habits/public/ - Публичные привычки
POST /api/habits/ - Создание привычки
PUT /api/habits/{id}/ - Обновление привычки
DELETE /api/habits/{id}/ - Удаление привычки
```

### Бизнес-логика

- Модель привычки описывается формулой: "Я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]"
- Валидаторы:
  - Время выполнения ≤ 120 секунд
  - Связанная привычка должна быть приятной
  - Нельзя одновременно указывать вознаграждение и связанную привычку
  - Приятная привычка не может иметь вознаграждения
  - Периодичность не реже 1 раза в 7 дней

### Интеграция с Telegram

- Создайте бота через @BotFather
- Добавьте токен в .env файл
- Напишите боту для получения chat_id
- Настройте периодические задачи в админке

### Тестирование

```bash
# Запуск тестов
python manage.py test

# Проверка покрытия
coverage run manage.py test
coverage report
```

### Проверка качества кода

```bash
# Flake8 проверка
flake8 . --exclude=migrations --max-line-length=120

# Проверка безопасности
python manage.py check --deploy
```

## Технологии

- Django 5.2 - Веб-фреймворк
- Django REST Framework - REST API
- Celery - Распределенные задачи
- Redis - Брокер сообщений
- JWT - Аутентификация
- Telegram Bot API - Уведомления
- Coverage - Анализ покрытия тестами

## Лицензия

MIT License - смотрите файл LICENSE для деталей.