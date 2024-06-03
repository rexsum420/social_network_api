from rest_framework import serializers
from .models import DirectMessage

class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = '__all__'

class CreateDirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = ['message', 'receiver']

    def create(self, validated_data):
        request = self.context.get('request')
        direct = DirectMessage.objects.create(
            sender=request.user,
            message = validated_data['message'],
            receiver = validated_data['receiver']
        )
        return direct