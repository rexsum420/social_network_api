from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class UserActivityLoggingMiddleware(MiddlewareMixin):
    """
    Middleware that logs User activity
    """

    def process_request(self, request):
        self.authenticate_user(request)
        self.update_active(request)
        self.update_ip_address(request)

    def authenticate_user(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return

        if len(auth) == 1:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth) > 2:
            raise AuthenticationFailed('Invalid token header. Token string should not contain spaces.')

        try:
            token = auth[1].decode()
        except UnicodeError:
            raise AuthenticationFailed('Invalid token header. Token string should not contain invalid characters.')

        try:
            token_obj = Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        request.user = token_obj.user

    def update_active(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            request.user.last_active = now()
            request.user.save()

    def update_ip_address(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            if ip_address and request.user.ip_address != ip_address:
                request.user.ip_address = ip_address
                request.user.save()
