from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    share = models.BooleanField(default=False)
    description = models.TextField(default="", null=True)
    cover_img = models.ImageField(upload_to="board_covers")

    pins = models.ManyToManyField('Pin')
    categories = models.ManyToManyField('Category')

    """
        Other Relations:
        1. user: many to many (owner) // to be done in user
        2. section: 1 to many (sections) // to be done in sections
        3. note: 1 to many (notes) // to be done in note
    """
