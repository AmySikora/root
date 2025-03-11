from django.db import models
from books.models import Book 
from django.utils import timezone

# Create your models here.
class Sale(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)  # Automatically set to now

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}"