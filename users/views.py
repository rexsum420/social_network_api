from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import AdminOnlyMixin
from rest_framework.authentication import TokenAuthentication

class UserViewSet(AdminOnlyMixin, viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()
