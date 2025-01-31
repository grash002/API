from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username  # Дополнительные данные в токене
        return token


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def update(self, instance, validated_data):
        # Создаем запись в истории
        UserProfileHistory.objects.create(
            user=instance,
            username=validated_data.get('username', instance.username),
            email=validated_data.get('email', instance.email),
            password_hash=instance.password if 'password' not in validated_data else instance.set_password(validated_data['password'])
        )

        # Обновляем текущего пользователя
        if 'username' in validated_data:
            instance.username = validated_data['username']

        if 'email' in validated_data:
            instance.email = validated_data['email']

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance