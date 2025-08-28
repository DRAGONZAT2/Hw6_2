from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate_published(self, value):
        if value > date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value
    
    class Meta:
        model = Book
        fields = '__all__'