from rest_framework import serializers
from pin.models import Pin, Category, Note, Section, PinNote, PinCategory, PinSection
from django.http.response import HttpResponse
from board.models import Board

from django.shortcuts import get_object_or_404


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        note = Note.objects.create(**validated_data)
        relation = PinNote.objects.create(pin=Pin.objects.get(
            pk=self.context.get("pin_id")), note=note)
        return note


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        relation = PinCategory.objects.create(pin=Pin.objects.get(
            pk=self.context.get("pin_id")), category=category)
        return category


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        section = Section.objects.create(**validated_data)
        relation = PinSection.objects.create(pin=Pin.objects.get(
            pk=self.context.get("pin_id")), section=section)
        return section


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'id', ]


class PinSerializer(serializers.ModelSerializer):
    #note = NoteSerializer(many=True)
    #category = CategorySerializer(many=True)
    #section = SectionSerializer(many=True)
    board = serializers.SerializerMethodField("get_board")

    class Meta:
        model = Pin
        fields = '__all__'
        # read_only_fields = ('board',)

    def create(self, validated_data):
        # example_relationship = validated_data.pop('example_relationship')
        # instance = ExampleModel.objects.create(**validated_data)
        # instance.example_relationship = example_relationship
        # return instance
        print(
            "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
        try:
            boards = get_object_or_404(Board, pk=self.context.get("board_id"))
            pin = Pin.objects.create(**validated_data)
            boards.pins.add(pin)
        except:
            pin = Pin.objects.create(**validated_data)

        return pin

    def get_board(self, instance: Pin):

        try:
            board = Board.objects.filter(pins=instance)[0]
            return BoardSerializer(board).data
        except:
            return "None"
        #board = get_object_or_404(Board, pins=instance)
