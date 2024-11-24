from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    ProtectedAPIView,
    ChangePasswordView,
    ActivateUserView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  # Регистрация
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),  # Авторизация
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('protected/', ProtectedAPIView.as_view(), name='protected-api'),  # Защищенный эндпоинт
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),  # Смена пароля
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),  # Активация аккаунта
]
