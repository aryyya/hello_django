from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=255)

    toppings = models.ManyToManyField('greeter.Topping')

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
