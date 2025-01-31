from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    LEVEL_CHOICES = [
        ('DEBUG', 'DEBUG'),
        ('INFO', 'INFO'),
        ('WARNING', 'WARNING'),
        ('ERROR', 'ERROR'),
        ('CRITICAL', 'CRITICAL'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    request_path = models.CharField(max_length=255, null=True, blank=True)
    request_method = models.CharField(max_length=10, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.level} - {self.timestamp} - {self.message}'


class UserProfileHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history")
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)  # Храним хеш пароля
    updated_at = models.DateTimeField(auto_now_add=True)  # Дата обновления

    def __str__(self):
        return f"{self.user.username} - {self.updated_at}"