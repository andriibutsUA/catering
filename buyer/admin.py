from django.contrib import admin
from .models import Ingredient, Dish, Recipe, TestDish, TestIngredient, TestRecipe

admin.site.register(Ingredient)

class DishInline(admin.TabularInline):
    model = Recipe
    extra = 1
    verbose_name = "Ингредиент"
    verbose_name_plural = "Ингредиенты"

class DishAdmin(admin.ModelAdmin):
    inlines = (DishInline,)

admin.site.register(Dish, DishAdmin)

class TestRecipeInline(admin.TabularInline):
    model = TestRecipe
    extra = 1

class TestDishAdmin(admin.ModelAdmin):
    inlines = (TestRecipeInline,)

class TestIngredientAdmin(admin.ModelAdmin):
    inlines = (TestRecipeInline,)

admin.site.register(TestDish, TestDishAdmin)
admin.site.register(TestIngredient, TestIngredientAdmin)