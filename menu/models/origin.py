from django.db import models
from .grower import Grower

class Origin(models.Model):

    # The visibility of the origin.
    visible = models.BooleanField(default=True)

    # The order of the origin (-1 for no ordering).
    order = models.IntegerField(default=-1)

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
        return f'{self.grower} ({self.city}, {self.state}, {self.country})'
