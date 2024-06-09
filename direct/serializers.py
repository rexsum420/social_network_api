from rest_framework import serializers
from .models import DirectMessage
from django.contrib.auth import get_user_model

class DirectMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for reading from the DirectMessage Model
    """
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()
    class Meta:
        model = DirectMessage
        fields = '__all__'

    def get_sender(self, obj):
        return obj.sender.username

    def get_receiver(self, obj):
        return obj.receiver.username

User = get_user_model()

class CreateDirectMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for creating DirectMessage objects
    """
    receiver = serializers.CharField()

    class Meta:
        model = DirectMessage
        fields = ['message', 'receiver']
    
    def validate_receiver(self, value):
        try:
            receiver = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")
        return receiver

    def create(self, validated_data):
        request = self.context.get('request')
        direct = DirectMessage.objects.create(
            sender=request.user,
            message=validated_data['message'],
            receiver=validated_data['receiver']
        )
        return direct