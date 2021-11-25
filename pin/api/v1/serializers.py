from rest_framework import serializers
from pin.models import Pin, PinCategory, Note, Section, PinNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
    
    def create(self, validated_data):
        note = Note.objects.create(**validated_data)
        relation = PinNote.objects.create(pin= Pin.objects.get(pk = self.context.get("pin_id")) , note= note )
        return note

class PinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PinCategory
        fields = ('name',)
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('name',)

class PinSerializer(serializers.ModelSerializer):
    note = NoteSerializer(many=True)
    PinCategory = PinCategorySerializer(many=True)
    PinSections = SectionSerializer(many=True)
    class Meta:
        model = Pin
        fields = '__all__'






