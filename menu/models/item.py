from .category import ItemCategory
from .origin import Origin
from .basic import Basic
from django.db import models
from datetime import datetime

class Item(Basic, models.Model):

    # The name of the item.
    name = models.CharField(max_length=64, unique=True)

    # The category of the item.
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

    # The stock level of the item.
    stock = models.CharField(max_length=16, choices=(('IN STOCK', 'In stock'), ('OUT OF STOCK', 'Out of stock'), ('RESTOCKING SOON', 'Restocking soon')), default='IN STOCK')

    # The translation of the item.
    translation = models.CharField(max_length=64, default='', blank=True)

    # The punchline of the item.
    punchline = models.CharField(max_length=64, default='', blank=True)

    # The bartender's notes on the item.
    bartender_notes = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class TeaItem(Item):

    # The origin of the item.
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    # The tasting notes of the item.
    tasting_notes = models.CharField(max_length=64, default='', blank=True)

    # The year of the item.
    year = models.CharField(max_length=4, default=datetime.now().year, blank=True)

    # The leaves of the item.
    leaves = models.CharField(max_length=64, default='', blank=True)

class FoodItem(Item):
    pass
