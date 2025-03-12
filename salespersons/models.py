from django.db import models
from django.contrib.auth.models import User  # Needed for OneToOneField

class Salesperson(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="salesperson"
    )  # Prevents deleting User when Salesperson is deleted
    name = models.CharField(max_length=120, default="Unknown Salesperson")
    bio = models.TextField(default="No bio...")  # Standardized default text

    def __str__(self):
        return f"{self.name} ({self.user.username if self.user else 'No User'})"
