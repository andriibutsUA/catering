from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    title = models.CharField(max_length=200)
    UNIT = (
        ('g', 'Грамм'),
        ('l', 'Литр'),
        ('q', 'Штуки'),
    )
    supplier = models.CharField(max_length=200)

    def __str__(self):
        return self.title