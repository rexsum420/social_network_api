from rest_framework import viewsets
from .models import BoardMessage
from .serializers import BoardMessageSerializer, CreateBoardMessageSerializer
from logs.models import UserLog
from social_network.permissions import ReadAndCreateOnlyMixin
from rest_framework.authentication import TokenAuthentication

class BoardMessageViewSet(ReadAndCreateOnlyMixin, viewsets.ModelViewSet):
    queryset = BoardMessage.objects.all()
    serializer_class = BoardMessageSerializer
    authentication_classes = (TokenAuthentication,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateBoardMessageSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        UserLog.objects.create(user=self.request.user, action='Sent a message to the board')