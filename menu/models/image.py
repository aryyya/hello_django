from django.db import models
from .basic import Basic

class Image(Basic, models.Model):

    name = models.CharField(max_length=255)

    data = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
