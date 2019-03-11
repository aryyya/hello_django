from django.db import models

class Grower(models.Model):
    name = models.CharField(max_length=64)
    notes = models.TextField(max_length=64)

    def __str__(self):
        return self.name
