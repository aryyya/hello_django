from django.db import models

class Basic(models.Model):
    
    # The visibility of the row.
    visible = models.BooleanField(default=True)

    # The order of the row.
    order = models.IntegerField(default=-1)

    class Meta:
        abstract = True
        ordering = ['order']
