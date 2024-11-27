from django.db import models
from django.contrib.auth import get_user_model

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(default="grams", max_length=20, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    instruction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredient = models.ManyToManyField(Ingredient, related_name="recipes")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = get_user_model()
    
    def __str__(self):
        return (self.name[:20])
    
# Dont forget to add notifications model someday 
    