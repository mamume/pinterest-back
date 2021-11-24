from django.db import models
from account.models import UserProfile


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    sender = models.ManyToManyField(UserProfile, related_name="sender")
    reciever = models.ManyToManyField(UserProfile, related_name="reciever")
