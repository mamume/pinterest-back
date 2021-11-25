# from django.conf import UserSettingsHolder
# from django.db.models import fields
from rest_framework import serializers
from .models import Board, Collaborator
from account.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', )


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'

    user = UserSerializer(many=True)


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        exclude = ["created_at", ]

    collaborators = CollaboratorSerializer(many=True)
