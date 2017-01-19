from django.db import models
from django.utils import timezone
from decimal import Decimal

class Ingredient(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    UNIT_CHOICES = (
        ('g', 'Грамм'),
        ('l', 'Литр'),
        ('q', 'Штуки'),
    )
    supplier = models.CharField(max_length=200, verbose_name="Поставщик")
    unit = models.CharField(
        max_length=1,
        choices=UNIT_CHOICES,
        default='g',
        verbose_name="Ед. измерения",
    )

    proteins = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Белки", default=Decimal('5.00'))
    fats = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Жиры", default=Decimal('5.00'))
    carbs = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Углеводы", default=Decimal('5.00'))

    def __str__(self):
        return self.title