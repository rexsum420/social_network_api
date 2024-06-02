from rest_framework import viewsets
from .models import DirectMessage
from .serializers import DirectMessageSerializer


class DirectMessageViewSet(viewsets.ModelViewSet):
    queryset = DirectMessage.objects.all()
    serializer_class = DirectMessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)