from .basic import Basic
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible


# Validators.

@deconstructible
class ValidateCoordinate:
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

    def __call__(self, coordinate):
        try:
            coordinate_as_float = float(coordinate)
            if coordinate_as_float < self.min or coordinate_as_float > self.max:
                raise ValueError
        except ValueError:
            raise ValidationError(f'{self.name} must be a number between {self.min} and {self.max}.')

# Models.

class Origin(Basic, models.Model):

    # The city of the origin.
    city = models.CharField(max_length=64)

    # The state of the origin.
    state = models.CharField(max_length=64)

    # The country of the origin.
    country = models.CharField(max_length=64)

    # The latitude of the origin.
    latitude = models.CharField(
        max_length=16,
        validators=[ValidateCoordinate('Latitude', -90.0, +90.0)]
    )

    # The longitude of the origin.
    longitude = models.CharField(
        max_length=16,
        validators=[ValidateCoordinate('Longitude', -180, +180)]
    )

    # The name of the grower.
    grower_name = models.CharField(max_length=64)

    # The notes about the grower.
    grower_notes = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.country}, {self.state}, {self.city} ({self.grower_name})'

    class Meta:
        unique_together = ('latitude', 'longitude')
