from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PokeSerializer
from Pokemon.models import Pokemondata
import json
# Create your views here.

class GetPokemon(APIView):

    def get(self, request, format=None):
        result = Pokemondata.objects.all()
        ser = PokeSerializer(result,many=True)
        if result.count() > 0:
            return Response({"msg":"Here are your pokemons","data":ser.data})
        else:
            return Response({"msg":"No pokemon found"})
class AddPokemon(APIView): 
    def post(self,request,format=None):
        result = Pokemondata(name=request.data['name'],attribute=request.data['attribute'],evolution=request.data['evolution'],height=request.data['height'],weight=request.data['weight'])
        result.save()
        return Response({"msg":"Pokemon added"})
        
class RemovePokemon(APIView):  
    def delete(self,request,name,format=None):
        print(request.data,name)
        res = Pokemondata.objects.filter(name=name).first()
        if res:
            res.delete()
            return Response({"msg":"Pokemon deleted"})
        else:
            return Response({"msg":"No pokemon found"})

class FindPokemon(APIView):
    def get(self,request,name,format=None):
        print(name)
        res = Pokemondata.objects.filter(name=name).first()
        res = PokeSerializer(res).data
        if res is not None and res["name"] !="":
            return Response({"msg":f"Here is info about {name}","data":res})
        else:
            return Response({"msg":f"Not found {name}"})


        
        
