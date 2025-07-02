from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
