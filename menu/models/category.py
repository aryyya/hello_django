from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class MenuCategory(Category):

    class Meta:
        verbose_name_plural = 'menu categories'

class ItemCategory(Category):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=64, default='')
    long_description = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'item categories'
