from rest_framework import serializers
from .models import Book, Review


class ReviewSer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'user_name', 'rating', 'text', 'created_at']
        read_only_fields = ['id', 'created_at', 'user_name']


class BookSer(serializers.ModelSerializer):
    reviews = ReviewSer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'published_date', 'average_rating', 'reviews']
