from django.db.models import fields
from rest_framework import serializers

from pin.models import Pin
from .models import Board, Collaborator, Note, Section
from account.models import UserProfile
from pin.api.v1.serializers import PinSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'profile_pic']


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'

    user = UserSerializer()


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "collaborators", "title", "share",
                  "description", "cover_img", "owner", 'pins']
        read_only_fields = ["collaborators", ]

    pins = serializers.SerializerMethodField('get_pins')

    def get_pins(self, instance: Board):
        serializer_context = {'request': self.context.get('request')}
        pins = Pin.objects.filter(board=instance)
        return PinSerializer(pins, many=True, context=serializer_context).data


class BoardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("pins", )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
