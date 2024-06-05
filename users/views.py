from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import AdminOnlyMixin

class UserViewSet(AdminOnlyMixin, viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user and user.is_authenticated:
            if user.is_staff:
                return CustomUser.objects.all()
            else:
                return CustomUser.objects.filter(id=user.id)
        return CustomUser.objects.none()

    def get_permissions(self):
        if self.request.method == 'POST':
            # Allow everyone to create an account
            return []
        return super().get_permissions()

    def get_authenticators(self):
        if self.request.method == 'POST':
            # Disable authentication for create action
            return []
        return super().get_authenticators()

    def perform_create(self, serializer):
        serializer.save()
