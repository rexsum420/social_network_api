from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from logs.models import UserLog

class UserActivityLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if request.path == '/api-token-auth/' and request.method == 'POST':
                UserLog.objects.create(user=request.user, action='Logged in', timestamp=datetime.now())
            elif request.path == '/logout/':
                UserLog.objects.create(user=request.user, action='Logged out', timestamp=datetime.now())
