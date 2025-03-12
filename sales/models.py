from django.db import models
from books.models import Book
from django.utils import timezone

def get_default_book():
   book = Book.objects.first()
   if book:
       return book.id
   # If no book exists, create one
   book = Book.objects.create(name="Default Book", price=9.99, genre="classic", book_type="hardcover")
   return book.id

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=get_default_book)  # Use default book ID
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=9.99)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}, price: {self.price}"
