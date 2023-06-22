from django.db import models
from django.conf import settings
# from autoslug import AutoSlugField
"""
-Global
    -Ingredients
    -Recipes

-User
    -Ingredients
    -Recipes
         -Ingredients
         -Directions for Ingredients

"""

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Topic(models.Model):
    title = models.CharField(max_length=200)
    # slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title
    

class Recipe(models.Model): # declaration of class

    # different fields

    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    # name = models.CharField(max_length=220)
    title = models.CharField(max_length=200)
    # slug = AutoSlugField(populate_from='title')
    image = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    ingredients = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # directions = models.TextField(blank=True, null=True)
    servings = models.CharField(max_length=5)
    time = models.IntegerField()
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # function to return name of record as title

    def __str__(self):
        return self.title
    
    
    def delete(self,*args, **kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE)
    name = models.CharField(max_length=220)
    quantity = models.CharField(max_length=50) #1 1/4
    unit =  models.CharField(max_length=50) #lbs, pounds oz, gram, etc
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    directions = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=recipe)


class GlobalIngredient(models.Model):
    name =  models.CharField(max_length=220)
    description =  models.TextField()


# class RecipeImage():
#     recipe = models.ForeignKey(Recipe)