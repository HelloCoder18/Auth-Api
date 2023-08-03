from rest_framework import serializers
from Recipes.models  import Recipe
class RecipeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Recipe
        fields = ('title','desc', 'author','date','id')

        