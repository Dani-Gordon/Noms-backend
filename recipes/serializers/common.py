from rest_framework import serializers
from ..models import *

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('__all__')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('__all__')


class RecipeIngredientSerializer(serializers.ModelSerializer):

    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity')


class DetailedRecipeSerializer(RecipeSerializer):

    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True)