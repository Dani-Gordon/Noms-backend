from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers.common import *
from jwt_auth.serializers import UserSerializer

# Create your views here.
class ListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()  #get all the recipes
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data) #send JSON to the user

class CreateView(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            # loop through ingredients 
            for ingredientId in request.data["ingredients"]:
                recipeIngredient = RecipeIngredient()
                recipeId = serializer.data["id"]
                recipeIngredient.recipe = Recipe.objects.get(pk=recipeId)
                recipeIngredient.ingredient = Ingredient.objects.get(pk=ingredientId)
                recipeIngredient.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailView(APIView): 
    def get(self, _request, pk):
        recipe = Recipe.objects.get(pk=pk) #get receipe by id
        serializer = DetailedRecipeSerializer(recipe)

        return Response(serializer.data) #send JSON to the user


class LikeView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):

        request.user.favorites.add(pk)
        request.user.save()

        return Response(status=status.HTTP_200_OK)

class LikedListView(APIView):

    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        recipes = request.user.favorites  #get all the liked recipes for user
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data) #send JSON to the user


class RemoveLikeView(APIView):

    permission_classes = (IsAuthenticated, )

    def put(self, request, pk):

        request.user.favorites.remove(pk)
        request.user.save()

        return Response(status=status.HTTP_200_OK)


class IngredientView(APIView):
    def get(self, request):
        recipes = Ingredient.objects.all()  #get all the ingredients
        serializer = IngredientSerializer(recipes, many=True)
        return Response(serializer.data) #send JSON to the user