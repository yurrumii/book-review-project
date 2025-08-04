from django.urls import path
from . import views

urlpatterns = [
    path('', views.some_view, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/reviews/add/', views.add_review, name='add_review'),
    path('logout/', views.logout_view, name='logout'),
]