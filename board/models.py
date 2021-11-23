from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    share = models.BooleanField(default=False)
    description = models.TextField(default="", null=True)
    cover_img = models.ImageField(upload_to="board_covers")
