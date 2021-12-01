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


class PinSerializer(serializers.ModelSerializer):
    #note = NoteSerializer(many=True)
    #category = CategorySerializer(many=True)
    #section = SectionSerializer(many=True)
    class Meta:
        model = Pin
        fields = '__all__'

    def create(self, validated_data):
        # example_relationship = validated_data.pop('example_relationship')
        # instance = ExampleModel.objects.create(**validated_data)
        # instance.example_relationship = example_relationship
        # return instance
        print(
            "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
        board = get_object_or_404(Board, pk=self.context.get("board_id"))
        pin = Pin.objects.create(**validated_data)
        board.pins.add(pin)
        return pin
