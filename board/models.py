from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BoardMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)