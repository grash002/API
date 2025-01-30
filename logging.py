import logging
from project.models import Log  # Импортируем модель, которую создали ранее

class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        from project.models import Log
        try:
            # Формируем сообщение лога
            log_message = self.format(record)
            level = record.levelname
            message = record.getMessage()

            # Записываем лог в базу данных
            Log.objects.create(level=level, message=message)
        except Exception as e:
            # Если произошла ошибка при записи в БД, можно записать её в стандартный лог
            print(f"Error logging to database: {e}")