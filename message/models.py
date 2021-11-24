from django.db import models
from account.models import UserProfile


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    sender = models.ManyToMany(UserProfile, on_delete=models.SET_NULL)
    reciever = models.ManyToMany(UserProfile, on_delete=models.SET_NULL)
