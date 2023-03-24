from django.db import models
from django.utils import timezone
from django.urls import reverse
# from taggit.managers import TaggableManager

Tags = (
    ("electronics", "electronics"),
    ("furniture", "furniture"),
    ("food", "food"),
    ("stationary", "stationary"),
    ("beverages", "beverages"),
    ("other", "other"),
)


class Orders(models.Model):
    name = models.TextField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    quantity = models.IntegerField()
    favorites = models.BooleanField(default=False)
    date_updated = models.DateTimeField(default=timezone.now)
    tags = models.CharField(
        max_length = 20,
        choices = Tags,
        default = 'other'
    )

    class Meta:
        ordering = ['-date_updated']

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})

