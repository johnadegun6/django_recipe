from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView

# Create your views here.
@api_view(['GET'])
def posts(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    data = serializer.data
    return Response(data, status=status.HTTP_200_OK)

elif request.method == 'POST':
    data = JSONParser.parse(request)
    serializer = PostSerializer(data=data, raise_exception= True)
    if serializer.is_valid():
    serializer.save()


class BlogPost(APIView):
    def get(self, request):
        pass

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'message': 'post created successfully'}, status=status.HTTP_201_CREATED)
