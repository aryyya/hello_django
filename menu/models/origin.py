from .basic import Basic
from django.core.exceptions import ValidationError
from django.db import models

# Validators.

def validate_coordinate(name, min, max):
    def validate(coordinate):
        try:
            coordinate_as_float = float(coordinate)
            if coordinate_as_float < min or coordinate_as_float > max:
                raise ValueError
        except ValueError:
            raise ValidationError(f'{name} must be a number between {min} and {max}.')
    return validate

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
        validators=[validate_coordinate('Latitude', -90.0, +90.0)]
    )

    # The longitude of the origin.
    longitude = models.CharField(
        max_length=16,
        validators=[validate_coordinate('Longitude', -180, +180)]
    )

    # The name of the grower.
    grower_name = models.CharField(max_length=64)

    # The notes about the grower.
    grower_notes = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.country}, {self.state}, {self.city} ({self.grower_name})'

    class Meta:
        unique_together = ('latitude', 'longitude')
