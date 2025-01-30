import logging
from django.db import models

# Обработчик логов для записи в базу данных
class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        try:
            from project.models import Log  # Импортируем модель в момент использования
            log_message = self.format(record)
            level = record.levelname
            message = record.getMessage()

            # Записываем лог в БД
            Log.objects.create(level=level, message=message)
        except Exception as e:
            # Если возникла ошибка при записи в БД, пишем в стандартный лог
            print(f"Error logging to database: {e}")