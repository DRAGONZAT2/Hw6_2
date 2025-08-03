from django.db import models
from django.conf import settings

class Pet(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    birth_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"
