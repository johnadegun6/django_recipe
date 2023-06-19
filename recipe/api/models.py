from django.db import models
# from autoslug import AutoSlugField
# Create your models here.

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
    

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    # slug = AutoSlugField(populate_from='title')
    image = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=5)
    timee = models.CharField(max_length=5)
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse("detail", kwargs={
            "slug": self.slug,
        })
    