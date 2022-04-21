from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers.common import *

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailView(APIView): 
    def get(self, _request, pk):
        recipe = Recipe.objects.get(pk=pk) #get receipe by id
        serializer = DetailedRecipeSerializer(recipe)

        return Response(serializer.data) #send JSON to the user


