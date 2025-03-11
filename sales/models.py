from django.db import models
from books.models import Book 

# Create your models here.
def get_default_book():
    return Book.objects.first().id

class Sale(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField()
	price = models.FloatField()
	date_created = models.DateTimeField(blank=True)


	def __str__(self):
		return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}"
