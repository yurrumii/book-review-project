from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(null=True, blank=True)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class Review(models.Model):
    objects = models.Manager()
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Мы будем использовать модель User от Django
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"