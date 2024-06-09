from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    name = models.CharField(max_length=128)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class BoardMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'