from rest_framework import viewsets
from .models import DirectMessage
from .serializers import DirectMessageSerializer, CreateDirectMessageSerializer
from social_network.permissions import ReadAndCreateOnlyMixin
from rest_framework.authentication import TokenAuthentication

class DirectMessageViewSet(ReadAndCreateOnlyMixin, viewsets.ModelViewSet):
    serializer_class = DirectMessageSerializer
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return DirectMessage.objects.filter(sender=self.request.user) | DirectMessage.objects.filter(receiver=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateDirectMessageSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)