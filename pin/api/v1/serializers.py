from rest_framework import serializers
from pin.models import Pin, PinCategory, Note, Section

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'

class PinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PinCategory
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'