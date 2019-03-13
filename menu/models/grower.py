from django.db import models

class Grower(models.Model):

    # The name of the grower.
    name = models.CharField(max_length=64)
    
    # The visibility of the grower.
    visible = models.BooleanField(default=True)

    # The order number of the grower (-1 for no ordering).
    order = models.IntegerField(default=-1)

    # The notes about the grower.
    notes = models.TextField(max_length=64)

    def __str__(self):
        return self.name
