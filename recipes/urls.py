from django.urls import path
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from .views import RecipeViewset, CategoryViewset, CommentViewset, IngredientViewset, FavoriteViewset

router = SimpleRouter()
router.register("recipes", RecipeViewset, basename="recipes")
router.register("categorys", CategoryViewset, basename="categorys")
router.register("comments", CommentViewset, basename="comments")
router.register("ingredients", IngredientViewset, basename="ingredients")
router.register("favorites", FavoriteViewset, basename="favorites")

urlpatterns = router.urls

