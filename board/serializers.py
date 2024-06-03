from rest_framework import serializers
from .models import BoardMessage

class BoardMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMessage
        fields = '__all__'

class CreateBoardMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMessage
        fields = ['message']

    def create(self, validated_data):
        request = self.context.get('request')
        board = BoardMessage.objects.create(
            user=request.user,
            message=validated_data['message'],
        )
        return board
