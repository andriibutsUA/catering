from django.contrib import admin
from .models import Ingredient, Dish, Recipe

admin.site.register(Ingredient)

class DishInline(admin.TabularInline):
    model = Recipe
    extra = 1
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
    inlines = (DishInline,)

admin.site.register(Dish, DishAdmin)