from django.db import models

# Genre choices
GENRE_CHOICES = (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational'),
)

# Book type choices
BOOK_TYPE_CHOICES = (
    ('hardcover', 'Hard cover'),
    ('ebook', 'E-Book'),
    ('audiobook', 'Audiobook'),
)

class Book(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120, blank=True, null=True)  # Allows empty values
    price = models.FloatField(default=9.99, help_text='In US dollars ($)')
    genre = models.CharField(max_length=12, choices=GENRE_CHOICES, default='classic')
    book_type = models.CharField(max_length=12, choices=BOOK_TYPE_CHOICES, default='hardcover')

    def __str__(self):
        return f"{self.name} by {self.author_name}" if self.author_name else self.name
