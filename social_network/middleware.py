from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from logs.models import UserLog

class UserActivityLoggingMiddleware(MiddlewareMixin):
    """
    Middleware that logs User activity
    """
    def process_request(self, request):
        if request.path == '/api-token-auth/' and request.method == 'POST':
            UserLog.objects.create(user=request.user, action='Logged in', timestamp=datetime.now())
            self.update_ip_address(request)
        elif request.path == '/logout/':
            UserLog.objects.create(user=request.user, action='Logged out', timestamp=datetime.now())

    def update_ip_address(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address and request.user.ip_address != ip_address:
            request.user.ip_address = ip_address
            request.user.save()
