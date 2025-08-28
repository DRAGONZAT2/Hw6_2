from django.db import models
from django.utils import timezone



# Create your models here.
class Book(models.Model):
     
     title = models.CharField(max_length=255)
     author = models.CharField(max_length=255)
     description = models.TextField()
     published = models.DateField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.title