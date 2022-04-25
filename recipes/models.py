from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name       

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)
    prep = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    directions = models.TextField(max_length=3000, null=True)
    image = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name 

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=1, null=True)

    def __str__(self):
        return f'{self.recipe.name} {self.ingredient.name} {self.quantity}'


