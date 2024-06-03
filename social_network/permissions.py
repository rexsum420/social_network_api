from rest_framework import permissions

class ReadAndCreateOnlyMixin:
    """
    Mixin that allows only admin users to PUT, PATCH, or DELETE.
    """
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method in ['GET', 'POST', 'OPTIONS']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()