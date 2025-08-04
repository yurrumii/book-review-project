from django.urls import path
from .views import BookListCreate, BookDetail, ReviewListCreate

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('books/<int:book_id>/reviews/', ReviewListCreate.as_view(), name='book-reviews'),
]