from django.db import models
from django.utils import timezone

class Items(models.Model):
    name = models.TextField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
    
