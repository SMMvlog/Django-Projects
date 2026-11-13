from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    book_id = serializers.CharField(write_only=True)
    class Meta:
        model = Book
        fields = '__all__'
