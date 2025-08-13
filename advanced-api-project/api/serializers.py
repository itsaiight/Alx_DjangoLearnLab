from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Serializers for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        # Validate that the publication year is not in the future
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to include books by the author
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'book'] 