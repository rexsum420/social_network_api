from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Board, BoardMessage
from .serializers import BoardMessageSerializer, CreateBoardMessageSerializer, BoardCreateSerializer, BoardReadOnlySerializer
from logs.models import UserLog
from social_network.permissions import ReadAndCreateOnlyMixin

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BoardCreateSerializer
        return BoardReadOnlySerializer

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
        UserLog.objects.create(user=self.request.user, action='Created a new board')

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
