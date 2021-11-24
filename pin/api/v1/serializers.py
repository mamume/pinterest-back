from rest_framework import serializers
from pin.models import Pin, PinCategory, Note, Section

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
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
        exclude = ('id',)






