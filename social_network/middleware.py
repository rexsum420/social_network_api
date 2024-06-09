from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from logs.models import UserLog
from django.utils.timezone import now

class UserActivityLoggingMiddleware(MiddlewareMixin):
    """
    Middleware that logs User activity
    """
    def log_user_activity(self, user, action):
        UserLog.objects.create(user=user, action=action, timestamp=now())

    def update_ip_address(self, request):
        ip_address = request.META.get('REMOTE_ADDR') 
        if ip_address and request.user.ip_address != ip_address:
            request.user.ip_address = ip_address
            request.user.save()
