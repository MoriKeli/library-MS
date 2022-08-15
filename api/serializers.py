from attr import field
from rest_framework import serializers
from staff.models import Book

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['ref_no', 'catalogue', 'title', 'author', 'published', 'publisher', 'publisher', 'type', 'rating']
