from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    question = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)