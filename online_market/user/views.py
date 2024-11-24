from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.urls import reverse
from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer
from .models import User

class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False  # Делаем пользователя неактивным до подтверждения
            user.save()

            # Отправка письма с подтверждением
            self.send_activation_email(user, request)

            return Response({'message': 'User registered successfully. Please check your email to activate your account.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_activation_email(self, user, request):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_link = request.build_absolute_uri(reverse('users:activate', args=[uid, token]))
        

        subject = 'Activate Your Account'
        message = f"""
        Hi {user.first_name},
        Please click the link below to activate your account:
        {activation_link}
        """
        email = EmailMessage(subject, message, to=[user.email])
        email.send()

class ActivateUserView(APIView):
    """
    Активация пользователя через подтверждение ссылки
    """
    def get(self, request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64)).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Account activated successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Activation link is invalid'}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Это защищенный API, доступный только с токеном."})

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Получаем старый и новый пароли из запроса
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        # Проверяем старый пароль
        if not check_password(old_password, user.password):
            return Response({"error": "Старый пароль неверен"}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем длину нового пароля
        if len(new_password) < 8:
            return Response({"error": "Новый пароль должен содержать не менее 8 символов"}, status=status.HTTP_400_BAD_REQUEST)

        # Устанавливаем новый пароль
        user.set_password(new_password)
        user.save()

        return Response({"success": "Пароль успешно изменен"}, status=status.HTTP_200_OK)
