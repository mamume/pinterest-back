from rest_framework import serializers
from pin.models import Pin, Category, Note, Section, PinNote, PinCategory, PinSection
from django.http.response import HttpResponse
from board.models import Board

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
    
    def create(self, validated_data):
        note = Note.objects.create(**validated_data)
        relation = PinNote.objects.create(pin= Pin.objects.get(pk = self.context.get("pin_id")) , note= note )
        return note

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        relation = PinCategory.objects.create(pin= Pin.objects.get(pk = self.context.get("pin_id")) , category=category )
        return category
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
    
    def create(self, validated_data):
        section = Section.objects.create(**validated_data)
        relation = PinSection.objects.create(pin= Pin.objects.get(pk = self.context.get("pin_id")) , section=section )
        return section

class PinSerializer(serializers.ModelSerializer):
    #note = NoteSerializer(many=True)
    #category = CategorySerializer(many=True)
    #section = SectionSerializer(many=True)
    class Meta:
        model = Pin
        fields = '__all__'
    

    def create(self, validated_data):
        print("((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
        boardId= self.context.get("board")
        board = Board.objects.get(pk= boardId)
        pin = Pin.objects.create(**validated_data, board_set=board)
        print(pin)
        return pin
        
    






