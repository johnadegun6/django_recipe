from rest_framework import serializers
from django.shortcuts import render
from rest_framework import viewsets
from .models import recipe
from api.models import Country
from .serializers import RecipeSerializer
from .models import Post
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class PostSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length = 255)
    # content = serializers.CharField
    # created_at = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Post.objects.create

    class Meta:
        model = Post
        fields = ('title', 'content')

class FoodPost_seriallizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['title',
                   'details',
                    'image',
                    'quantity',
                    'category',
                    'location',
                    'price',
                    'created_post',
                    'status',
                    ]


    def create(self,validated_data):
        # print()
        # print(validated_data)

        foodPost = Post(**validated_data,user=self.context.get("user"))
        foodPost.save()
        # foodPost.save()
        return foodPost


class RecipeSerializer(serializers.ModelSerializer):
   class Meta: #to create the JSON fields
       model = recipe
       fields = ('id','name','ingriedient ','time','process')




class CountryModelSerializer(serializers.ModelSerializer):
    """Country Model Serializer"""

    class Meta:
        """Meta class"""
        model = Country
        fields = (
            'id',
            'name',
            'image'
        )