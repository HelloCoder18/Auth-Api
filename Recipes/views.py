from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RecipeSerializer
from Recipes.models import Recipe
import json
# Create your views here.

class GetRecipe(APIView):

    def get(self, request, format=None):
        print("hello")
        result = Recipe.objects.all()
        ser = RecipeSerializer(result,many=True)
        if result.count() > 0:
            return Response({"msg":"Here are your recipes","data":ser.data})
        else:
            return Response({"msg":"No recipe found"})
class AddRecipe(APIView): 
    def post(self,request,format=None):
        result = Recipe(title=request.data["title"],author=request.data["author"],desc=request.data["desc"])
        result.save()
        return Response({"msg":"recipe added"})
        
class RemoveRecipe(APIView):  
    def get(self,request,format=None):
        res=Recipe.objects.all()
        if res:
            res.delete()
            return Response({"msg":"all recipe deleted"})
        else:
            return Response({"msg":"No recipe found"})
        
    def delete(self,request,author,id,format=None):
        print(request.data,id)
        res = Recipe.objects.filter(author=author,id=id).first()
        if res:
            res.delete()
            return Response({"msg":"recipe deleted"})
        else:
            return Response({"msg":"No recipe found"})

class FindRecipe(APIView):
    def get(self,request,author,format=None):
        print(author)
        res = Recipe.objects.filter(author=author)
        if res.count() > 0:
            res = RecipeSerializer(res,many=True).data
        else:
            res = None
        if res is not None:
            return Response({"msg":f"Here are all recipes of {author}","data":res})
        else:
            return Response({"msg":f"Not found any recipe of {author}"})


        
        
