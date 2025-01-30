from rest_framework_simplejwt.views import TokenObtainPairView
from project.serializers import CustomTokenObtainPairSerializer, UpdateUserSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Пользователь создан"}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Только для аутентифицированных пользователей

    def put(self, request, *args, **kwargs):
        user = request.user  # Получаем текущего аутентифицированного пользователя
        serializer = UpdateUserSerializer(user, data=request.data, partial=True)  # частичное обновление

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)