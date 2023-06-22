from django.urls import re_path
from django.urls import path, include
from. import views
from api.locations.views import countries as country_views
from rest_framework.routers import DefaultRouter
from .views import home, search, detail
from rest_framework import routers
from rest_framework import viewsets
from api.serializers import CountryModelSerializer
from api.models import Country


router = routers.DefaultRouter()
router.register('recipe',views.RecipeView) #registering routers.

router = DefaultRouter
router.register(r'countries', country_views.CountryViewSet, basename='country')

urlpatterns = router.urls


urlpatterns = [
    re_path(r'^posts/$', views.BlogPost.as_view(), name= 'posts'),
    #re_path(r'^posts/?p<pk>),
    path("", home, name='home'),
    path("search", search, name='search'),
    path("<slug>", detail, name='detail'),
    path('',include(router.urls)),
]


class CountryViewSet(viewsets.ModelViewSet):
    """Country viewset"""

    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer