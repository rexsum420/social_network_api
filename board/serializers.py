from rest_framework import serializers
from .models import Board, BoardMessage

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
            board=validated_data['board']  # Ensure the board is included in the validated data
        )
        return board

class BoardCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating Board objects
    """
    class Meta:
        model = Board
        fields = ['name']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['admin'] = request.user
        return super().create(validated_data)


class BoardReadOnlySerializer(serializers.ModelSerializer):
    admin = serializers.StringRelatedField()
    messages = BoardMessageSerializer(many=True, read_only=True, source='boardmessage_set')

    class Meta:
        model = Board
        fields = ['id', 'name', 'admin', 'messages']
