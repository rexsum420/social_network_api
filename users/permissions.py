from rest_framework import permissions

class AdminOnlyMixin:
    """
    Mixin that allows only admin users to PUT, PATCH, or DELETE.
    """
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        elif self.action in ['list', 'retrieve', 'create']:
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()
