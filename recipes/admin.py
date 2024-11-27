from django.contrib import admin
from .models import Category, Ingredient, Comment, Recipe

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Comment)
admin.site.register(Recipe)
