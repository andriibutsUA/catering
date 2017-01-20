from django.db import models
from decimal import Decimal


class Ingredient(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    UNIT_CHOICES = (
        ('g', 'Грамм'),
        ('l', 'Литр'),
        ('q', 'Штуки'),
    )
    CATEGORY_CHOICES = (
        ('1', 'Грибы'),
        ('2', 'Колбасные изделия'),
        ('3', 'Крупы и каши'),
        ('4', 'Масла и жиры'),
        ('5', 'Яйца'),
        ('6', 'Ягоды'),
        ('7', 'Фрукты'),
        ('8', 'Молочные продукты'),
        ('9', 'Мука и макаронные изделия'),
        ('10', 'Орехи и сухофрукты'),
        ('11', 'Мясопродукты'),
        ('12', 'Овощи и зелень'),
        ('13', 'Рыба и морепродукты'),
        ('14', 'Сыры и творог'),
        ('15', 'Хлебобулочные изделия'),
        ('16', 'Напитки алкогольные'),
        ('17', 'Напитки безалкогольные'),
        ('18', 'Соки и компоты'),
    )
    first_supplier = models.CharField(max_length=200, verbose_name="Поставщик 1", default="Novus")
    second_supplier = models.CharField(max_length=200, verbose_name="Поставщик 2", default="Novus")
    third_supplier = models.CharField(max_length=200, verbose_name="Поставщик 3", default="Novus")
    unit = models.CharField(
        max_length=1,
        choices=UNIT_CHOICES,
        default='g',
        verbose_name="Ед. измерения",
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='1',
        verbose_name="Категория",
        )
    proteins = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Белки", default=Decimal('5.00'))
    fats = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Жиры", default=Decimal('5.00'))
    carbs = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Углеводы", default=Decimal('5.00'))
    calories = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Калории", default=Decimal('5.00'))

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    gross = models.PositiveIntegerField(verbose_name="Брутто", default=50)
    description = models.TextField(verbose_name="Рецепт и описание")
    dish_ingredient = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        blank=True,
                                        null=True,
                                        verbose_name="Блюдо в качестве ингредиента"
                                        )
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ингредиенты")
    CATEGORY_CHOICES = (
        ('1', 'Холодные закуски'),
        ('2', 'Закуски'),
        ('3', 'Горячие закуски'),
        ('4', 'Вторые блюда'),
        ('5', 'Гарниры'),
        ('6', 'Десерты'),
        ('7', 'Барбекю'),
        ('8', 'Напитки'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='2',
        verbose_name="Категория"
    )

    def __str__(self):
        return self.title
