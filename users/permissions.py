from rest_framework import permissions

class AdminOnlyMixin:
    """
    Mixin that allows only admin users to PUT, PATCH, or DELETE.
    """
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method in ['POST']:
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()