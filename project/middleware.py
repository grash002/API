import logging

logger = logging.getLogger('django')

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем информацию о запросе
        logger.info(f'API Request: {request.method} {request.path}')
        response = self.get_response(request)
        return response