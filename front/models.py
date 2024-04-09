from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 50, blank = False)
    description = models.TextField(max_length = 300, blank = False)