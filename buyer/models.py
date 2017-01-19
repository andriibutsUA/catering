from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    title = models.CharField(max_length=200)
    unit = models.
    UNIT_CHOICES = (
        ('g', 'Грамм'),
        ('l', 'Литр'),
        ('q', 'Штуки'),
    )
    supplier = models.CharField(max_length=200)
    unit = models.CharField(
        max_length=1,
        choices=UNIT_CHOICES,
    )

    def __str__(self):
        return self.title