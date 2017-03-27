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
        ('19', 'Приправы и специи'),
        ('20', 'Разное'),
    )
    first_supplier = models.CharField(max_length=200, verbose_name="Производитель 1", default="Novus")
    second_supplier = models.CharField(max_length=200, verbose_name="Производитель 2", default="Novus")
    third_supplier = models.CharField(max_length=200, verbose_name="Производитель 3", default="Novus")
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
    proteins = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Белки", default=Decimal('0.00'))
    fats = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Жиры", default=Decimal('0.00'))
    carbs = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Углеводы", default=Decimal('0.00'))
    calories = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Калории", default=Decimal('0.00'))

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Рецепт и описание", blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, through="Recipe", verbose_name="Ингредиенты")
    weight = models.PositiveIntegerField(verbose_name="Вес", default="1")
    sauce = models.ForeignKey("self", verbose_name="Соус", limit_choices_to={'category': '9'}, blank=True, null=True)
    sauce_q = models.PositiveIntegerField(default="0", verbose_name="Количество соуса")
    CATEGORY_CHOICES = (
        ('1', 'Холодные закуски'),
        ('2', 'Закуски'),
        ('3', 'Горячие закуски'),
        ('4', 'Вторые блюда'),
        ('5', 'Гарниры'),
        ('6', 'Десерты'),
        ('7', 'Барбекю'),
        ('8', 'Напитки'),
        ('9', 'Соусы'),
        ('10', 'Спорт'),
        ('11', 'Канапе'),
        ('12', 'Салаты'),
        ('13', 'Намазки'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='2',
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.title


class Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name="Ингредиент")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default="10", verbose_name="Брутто")

    def __str__(self):
        return "Ингредиент для " + str(self.dish)


class BuyerListIntermediate(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default="1")


class BuyerList(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    dishes = models.ManyToManyField(BuyerListIntermediate, verbose_name="Блюда")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Список закупщика"
        verbose_name_plural = "Ингредиенты"