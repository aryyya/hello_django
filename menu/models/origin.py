from django.db import models
from .grower import Grower

class Origin(models.Model):
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    latitude = models.CharField(max_length=32)
    longitude = models.CharField(max_length=32)
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.grower} ({self.city}, {self.state}, {self.country})'
