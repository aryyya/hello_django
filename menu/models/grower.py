from django.db import models
from .basic import Basic

class Grower(Basic, models.Model):

    # The name of the grower.
    name = models.CharField(max_length=64)

    # The notes about the grower.
    notes = models.TextField(max_length=64, default='', blank=True)

    def __str__(self):
        return self.name
