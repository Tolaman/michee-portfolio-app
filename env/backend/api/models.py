from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='projects/', blank=True, default='projects/default.png')
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

class Service(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='services/', blank=True)

class Experience(models.Model):
    title = models.CharField(max_length=155)
    company = models.CharField(max_length=155)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='experiences/', blank=True, default='experiences/default.png')

