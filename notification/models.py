from django.db import models
from account.models import UserProfile


class Notification(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
