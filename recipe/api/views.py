from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from api.views import countries as country_views
from .serializers import PostSerializer
from .serializers import RecipeSerializer
from .models import Post, recipe
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView
from django.db.models import Q
from .models import Recipe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
@api_view(['GET'])
def posts(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    data = serializer.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
# @parser_classes([JSONParser,FormParser,MultiPartParser])
def create_post(request):

    serializer = Post_serializer(data = request.data,context = {"user":request.user})
    if serializer.is_valid(raise_exception=True):
        foodpost = serializer.save()
        return Response(serializer.data)
    

# elif request.method == 'POST':
#     data = JSONParser.parse(request)
#     serializer = PostSerializer(data=data, raise_exception= True)
#     if serializer.is_valid():
#     serializer.save()


class BlogPost(APIView):
    def get(self, request):
        pass

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'message': 'post created successfully'}, status=status.HTTP_201_CREATED)



def home(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        "title" : "Homepage",
        "total_recipes":total_recipes,
    }
    return render(request, "home.html", context)


def search(request):
    recipes =  Recipe.objects.all()

    if 'search' in request.GET:
        query = request.GET.get('search')
        queryset = recipes.filter(Q(title_icontains=query))
    
    if request.GET.get("breakfast"):
        results = queryset.filter(Q(topic_title_icontains='breakfast'))
        topic = "breakfast"
    elif request.GET.get("appetizers"):
        results = queryset.filter(Q(topic_title_icontains='appetizers'))
        topic = "appetizers"
    elif request.GET.get("launch"):
        results = queryset.filter(Q(topic_title_icontains='lunch'))
        topic = "launch"
    elif request.GET.get("salads"):
        results = queryset.filter(Q(topic_title_icontains='salads'))
        topic = "salads"
    elif request.GET.get("dinner"):
        results = queryset.filter(Q(topic_title_icontains='dinner'))
        topic = "dinner"
    elif request.GET.get("dessert"):
        results = queryset.filter(Q(topic_title_icontains='dessert'))
        topic = "dessert"
    elif request.GET.get("easy"):
        results = queryset.filter(Q(topic_title_icontains='easy'))
        topic = "easy"
    elif request.GET.get("hard"):
        results = queryset.filter(Q(topic_title_icontains='hard'))
        topic = "harder"


    total = results.count()
    
    #paginate results
    paginator = Paginator(results, 3)
    page = request.GET.get("page")

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page()    
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "topic": topic,
        "page": page,
        "total": total,
        "query": query,
        "results" : results,
    }
    return render(request, "search.html", context)

def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug = slug)
    context = {
        "recipe": recipe,
    }
    return render(request, "detail.html", context)

def recipe(request):
    return render(request, 'recipe.html')


class RecipeView(viewsets.ModelViewSet):
     queryset= recipe.objects.all() #spit out all the fields
     serializer_class= RecipeSerializer