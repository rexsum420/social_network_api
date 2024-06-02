from rest_framework import serializers
from .models import BoardMessage

class BoardMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMessage
        fields = '__all__'