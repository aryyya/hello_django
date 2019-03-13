from .category import ItemCategory
from .origin import Origin
from django.db import models
from datetime import datetime

class Item(models.Model):
    name = models.CharField(max_length=64)
    translation = models.CharField(max_length=64, default='')
    punchline = models.CharField(max_length=64, default='')
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=64)
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=-1)
    stock = models.CharField(max_length=16, choices=(('IN STOCK', 'In stock'), ('OUT OF STOCK', 'Out of stock'), ('RESTOCKING SOON', 'Restocking soon')), default='IN STOCK')
    bartender_notes = models.TextField(default='')

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class TeaItem(Item):
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    tasting_notes = models.CharField(max_length=64, default='')
    year = models.CharField(max_length=4, default=datetime.now().year)
    leaves = models.CharField(max_length=64, default='')

class FoodItem(Item):
    pass
