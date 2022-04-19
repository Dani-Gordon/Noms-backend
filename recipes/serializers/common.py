from rest_framework import serializers
from ..models import *

class RecipeIngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredients
        fields = ('__all__')
        
class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('__all__')

class IngredientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Ingredient
        fields = ('__all__')

        RecipeIngredients = RecipeIngredientsSerializer(many=True)

class DetailedRecipeSerializer(RecipeSerializer):
        ingredients = IngredientSerializer(many=True)


