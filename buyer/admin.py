from django.contrib import admin
from .models import Ingredient, Dish, Recipe, TestDish, TestIngredient, TestRecipe

admin.site.register(Ingredient)

class DishInline(admin.TabularInline):
    model = Recipe
    extra = 1
    verbose_name = "Ингредиент"
    verbose_name_plural = "Ингредиенты"
    class Media:
        css = {
            "all": ("http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.1/themes/ui-lightness/jquery-ui.css",)
        }
        js = ("https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js","https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.js", "js/main.js")

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