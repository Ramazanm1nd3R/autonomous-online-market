from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager  # Импортируйте менеджер из managers.py

class User(AbstractUser):
    username = None  # Удаляем поле username
    email = models.EmailField(unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()  # Подключаем кастомный менеджер

    def __str__(self):
        return self.email
