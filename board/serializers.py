from rest_framework import serializers
from .models import Board, Collaborator
from account.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'

    user = UserSerializer()


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "collaborators", "title", "share",
                  "description", "cover_img", "owner"]
        read_only_fields = ('cover_img',)
