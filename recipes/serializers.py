from .models import Recipe, Comment, Category, Ingredient, Favorite
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField() 
    class Meta:
        model = Recipe
        fields = '__all__' 
    def get_created_by(self, obj):
        if obj.created_by:  # Check if created_by exists
            return {
                "id": obj.created_by.id,
                "username": obj.created_by.username
            }
        return None
        
class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField() 
    class Meta:
        model = Category
        fields = '__all__'
        
    def get_created_by(self, obj):
        if obj.created_by:  # Check if created_by exists
            return {
                "id": obj.created_by.id,
                "username": obj.created_by.username
            }
        return None
class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField() 
    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:  # Check if created_by exists
            return {
                "id": obj.created_by.id,
                "username": obj.created_by.username
            }
        return None
class IngredientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField() 
    class Meta:
        model = Ingredient
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:  # Check if created_by exists
            return {
                "id": obj.created_by.id,
                "username": obj.created_by.username
            }
        return None
    
class FavoriteSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField() 
    class Meta:
        model = Favorite
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:  # Check if created_by exists
            return {
                "id": obj.created_by.id,
                "username": obj.created_by.username
            }
        return None
    
        
    