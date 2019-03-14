from django.db import models
from .basic import Basic

class Origin(Basic, models.Model):

    # The city of the origin.
    city = models.CharField(max_length=64)

    # The state of the origin.
    state = models.CharField(max_length=64)

    # The country of the origin.
    country = models.CharField(max_length=64)

    # The latitude of the origin.
    latitude = models.CharField(max_length=32)

    # The longitude of the origin.
    longitude = models.CharField(max_length=32)

    # The name of the grower.
    grower_name = models.CharField(max_length=64)

    # The notes about the grower.
    grower_notes = models.TextField(max_length=64, default='', blank=True)

    def __str__(self):
        return f'{self.country}, {self.state}, {self.city} ({self.grower_name})'

    class Meta:
        unique_together = ('latitude', 'longitude')
