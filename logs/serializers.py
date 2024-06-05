from rest_framework import serializers
from .models import UserLog

class UserLogSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserLog Model
    """
    class Meta:
        model = UserLog
        fields = '__all__'