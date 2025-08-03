from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Pet
        fields = ['id', 'name', 'type', 'birth_date', 'owner', 'created_at']
