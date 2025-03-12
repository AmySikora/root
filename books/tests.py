from django.test import TestCase
from books.models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):  # Runs once before all test methods
        cls.book = Book.objects.create(
            name='Pride and Prejudice', 
            price=23.71,
            genre='classic', 
            book_type='hardcover'
        )

    def test_book_name(self):
        field_label = self.book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_book_price(self):
        self.assertEqual(self.book.price, 23.71)
