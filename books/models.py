from django.db import models, reverse

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
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    def __str__(self):
        return f"{self.name} by {self.author_name}" if self.author_name else self.name
    
    def get_absolute_url(self):
       return reverse ('books:detail', kwargs={'pk': self.pk})
