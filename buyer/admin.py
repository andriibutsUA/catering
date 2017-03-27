from django.contrib import admin
from .models import Ingredient, Dish, Recipe, BuyerList


class DishInline(admin.TabularInline):
    model = Recipe
    extra = 0
    verbose_name = "Ингредиент"
    verbose_name_plural = "Ингредиенты"

    class Media:
        css = {
            "all": (
                "http://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css",
                "css/admin.css"
                )
        }
        js = (
                "https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js",
                "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.js",
                "js/main.js",
             )


class DishAdmin(admin.ModelAdmin):

    class Media:
        css = {
            "all": ("css/admin.css",)
        }
    inlines = (DishInline,)
    list_filter = ['category']
    list_display = ('title', 'weight',)
    search_fields = ['title']


class IngredientAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/admin.css",)
        }

    list_filter = ('category',)
    search_fields = ['title']

admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)