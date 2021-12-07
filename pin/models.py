from django.db import models
from account.models import UserProfile

# Create your models here.

share_type = (
    ('Public', 'Public'),
    ('Private', 'Private'),
)

content_type = (
    ('image', 'image'),
    ('video', 'video'),
)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    # checklist -- array of items

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pin(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    content_type = models.CharField(max_length=15, choices=content_type)
    external_website = models.URLField(max_length=200, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    alt_text = models.CharField(max_length=500, blank=True)
    content_src = models.ImageField(
        upload_to='pins/')
    share_type = models.CharField(
        max_length=15, choices=share_type, blank=True)
    category = models.ManyToManyField('Category', through='PinCategory')
    note = models.ManyToManyField('Note', through='PinNote')
    section = models.ManyToManyField('Section', through='PinSection')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-creation_date"]


class PinNote(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE,)
    note = models.ForeignKey(Note, on_delete=models.CASCADE,)


class PinSection(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE,)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,)


class PinCategory(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
