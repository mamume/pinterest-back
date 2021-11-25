from django.db.models import fields
from rest_framework import serializers
from .models import Board, Collaborator


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'share', 'description',
                  'collaborators', 'cover_img']

    collaborators = CollaboratorSerializer()
