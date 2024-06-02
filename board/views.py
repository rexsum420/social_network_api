from rest_framework import viewsets
from .models import BoardMessage
from .serializers import BoardMessageSerializer
from logs.models import UserLog
from logs.serializers import UserLogSerializer

class BoardMessageViewSet(viewsets.ModelViewSet):
    queryset = BoardMessage.objects.all()
    serializer_class = BoardMessageSerializer

    def perform_create(self, serializer):
        board_message = serializer.save(user=self.request.user)
        UserLog.objects.create(user=self.request.user, action='Sent a message to the board')
