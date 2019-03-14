from django.db import models
from .grower import Grower
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

    # The grower at the origin.
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country}, {self.state}, {self.city} ({self.grower})'

    class Meta:
        unique_together = ('latitude', 'longitude')
