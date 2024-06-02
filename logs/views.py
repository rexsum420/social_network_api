from rest_framework import viewsets
from .models import UserLog
from .serializers import UserLogSerializer

class UserLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer