from django.db.models import Avg
from rest_framework import generics
from .models import Book, Review
from .serializers import BookSer, ReviewSer


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-average_rating')
    serializer_class = BookSer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSer



class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id).order_by('-created_at')

    def perform_create(self, serializer):
        book_id = self.kwargs['book_id']
        book = Book.objects.get(id=book_id)
        serializer.save(book=book)


        average_rating = book.reviews.aggregate(Avg('rating'))['rating__avg']
        book.average_rating = round(average_rating, 2) if average_rating is not None else 0.0
        book.save()
