from rest_framework import serializers
from .models import BoardMessage

class BoardMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for reading from the BoardMessage Model
    """
    user = serializers.SerializerMethodField()
    class Meta:
        model = BoardMessage
        fields = '__all__'
    def get_user(self, obj):
        return obj.user.username

class CreateBoardMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for creating BoardMessage objects
    """
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
