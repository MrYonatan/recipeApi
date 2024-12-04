from rest_framework import viewsets
from .models import Recipe, Comment, Category, Ingredient, Favorite
from .serializers import RecipeSerializer, CategorySerializer, CommentSerializer, IngredientSerializer, FavoriteSerializer
from .permissions import IsAuthorOrReadOnly
from accounts.models import CustomUser

class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthorOrReadOnly]

class IngredientViewset(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
class FavoriteViewset(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_staff :
            return Favorite.objects.all()
        return self.queryset.filter(id=self.request.user.id)
    