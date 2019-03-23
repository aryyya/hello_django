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

class Musician(models.Model):
    name = models.CharField(max_length=255)

    instrument = models.CharField(max_length=255, choices=(
        ('guitar', 'Guitar'),
        ('bass', 'Bass'),
        ('drums', 'Drums'),
        ('vocals', 'Vocals'),
        ('brass', 'Brass'),
        ('piano', 'Piano')
    ))

    band = models.ManyToManyField('Band', through='Member')

    def __str__(self):
        return self.name

class Member(models.Model):
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)

    band = models.ForeignKey('Band', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.band.name} ({self.musician.name})'

class Band(models.Model):
    name = models.CharField(max_length=255)

    genre = models.CharField(max_length=255, choices=(
        ('rock', 'Rock'),
        ('hip-hop', 'Hip Hop'),
        ('jazz', 'Jazz')
    ))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(f'{self.name} is a cool band!')
        super().save(*args, **kwargs)

    @property
    def intro(self):
        return f'{self.name} is a {self.genre} group with {self.member_set.count()} members.'
