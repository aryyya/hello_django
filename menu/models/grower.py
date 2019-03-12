from django.db import models

class Grower(models.Model):
    name = models.CharField(max_length=64)
    notes = models.TextField(max_length=64)
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=-1)

    def __str__(self):
        return self.name
