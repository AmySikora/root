from django.db import models
from django.contrib.auth.models import User #needed for OneToOneField

# Create your models here.
class Salesperson(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)  # Don't delete User
    name = models.CharField(max_length=120, default="Unknown Salesperson")
    bio = models.TextField(default="no bio...")

    def __str__(self):
        return f"{self.name} ({self.user.username if self.user else 'No User'})"
		# f-string allows to format the string, so for username abc, you will see: Profile of abc  s