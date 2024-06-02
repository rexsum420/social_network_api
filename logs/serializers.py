from rest_framework import serializers
from .models import UserLog

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = '__all__'