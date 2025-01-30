import logging
from project.models import Log  # импортируем вашу модель логов

logger = logging.getLogger('django')

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем запрос в таблицу project_log
        Log.objects.create(
            level='INFO',  # можно добавить любой уровень логирования
            message=f'API Request: {request.method} {request.path}',
            request_path=request.path,
            request_method=request.method,
            user_name=request.user.username if request.user.is_authenticated else 'Anonymous'
        )

        response = self.get_response(request)
        return response