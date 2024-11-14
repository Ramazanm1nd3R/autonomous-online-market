from rest_framework import status, views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password

class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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