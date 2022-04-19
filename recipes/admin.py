from django.contrib import admin

from recipes.models import Ingredient, Recipe, RecipeIngredients

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredients)