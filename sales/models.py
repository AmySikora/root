from django.db import models
from books.models import Book 

# Create your models here.

def get_default_book():
    default_book = Book.objects.first() 
    return default_book.id if default_book else None

class Sale(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField()
	price = models.FloatField()
	date_created = models.DateTimeField(blank=True)


	def __str__(self):
		return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}"
