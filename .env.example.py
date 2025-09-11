# Django
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=habittracker
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Telegram Bot
TELEGRAM_BOT_TOKEN=your-telegram-bot-token

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
