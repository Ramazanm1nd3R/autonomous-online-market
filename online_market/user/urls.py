from django.urls import path
from .views import UserRegistrationView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProtectedAPIView, ChangePasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedAPIView.as_view(), name='protected-api'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password')
]
