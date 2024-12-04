from django.contrib import admin
from .models import Category, Ingredient, Comment, Recipe, Favorite

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Favorite)