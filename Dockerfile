# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости для сборки (например, gcc, psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Скопировать requirements.txt в контейнер
COPY requirements.txt /app/

# Установить зависимости Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Скопировать проект Django (всю папку online_market) в рабочую директорию контейнера
COPY online_market /app/online_market

# Указываем рабочую директорию как директорию Django проекта
WORKDIR /app/online_market

# Открыть порт 8000 для внешнего доступа
EXPOSE 8000

# Команда для запуска Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
