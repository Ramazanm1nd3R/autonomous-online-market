# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости для сборки (например, gcc, psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Скопировать файлы requirements в контейнер
COPY requirements.txt /app/

# Установить зависимости Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Скопировать весь проект в рабочую директорию контейнера
COPY . /app/

# Открыть порт 8000
EXPOSE 8000

# Команда для запуска сервера разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
