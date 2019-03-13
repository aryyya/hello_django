from django.db import models
from .basic import Basic

class Category(Basic, models.Model):

    # The name of the category.
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class MenuCategory(Category):

    class Meta:
        verbose_name_plural = 'menu categories'

class ItemCategory(Category):

    # The menu category of the item category.
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    # The short description of the item category.
    short_description = models.CharField(max_length=64, default='')

    # The long description of the item category.
    long_description = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'item categories'
