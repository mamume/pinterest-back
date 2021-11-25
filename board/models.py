from django.db import models
from account.models import UserProfile


class Board(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    share = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    cover_img = models.ImageField(
        upload_to="board/covers", null=True, blank=True)

    # pins = models.ManyToManyField('Pin')
    collaborators = models.ManyToManyField('Collaborator', blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Collaborator(models.Model):
    # boards = models.ManyToManyField(Board)
    user = models.OneToOneField(
        UserProfile, primary_key=True, on_delete=models.CASCADE)
    is_super = models.BooleanField(default=False)
    can_invite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True)
    ckeck_list = models.JSONField(null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
