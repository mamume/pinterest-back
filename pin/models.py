from django.db import models

# Create your models here.

share_type = (
('Public','Public'),
('Private','Private'),
)

content_type = (
('image','image'),
('video','video'),
)

class PinCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Note(models.Model):
    title = models.CharField(max_length=100)
    #checklist -- array of items

    def __str__(self):
        return self.title

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Pin(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    content_type = models.CharField(max_length=15,choices=content_type)
    external_website= models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    alt_text = models.CharField(max_length=500)
    content_src = models.URLField(max_length=200)
    share_type = models.CharField(max_length=15,choices=share_type)
    PinCategory = models.ManyToManyField('PinCategory')
    note = models.ManyToManyField('Note', through='PinNote')
    PinSections = models.ManyToManyField('Section')

    
    def __str__(self):
        return self.title
class PinNote(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE,) 
    note = models.ForeignKey(Note, on_delete=models.CASCADE,)


