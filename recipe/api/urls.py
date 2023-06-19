from django.urls import re_path
from django.urls import path
from. import views
from .views import home, search, detail

urlpatterns = [
    re_path(r'^posts/$', views.BlogPost.as_view(), name= 'posts'),
    #re_path(r'^posts/?p<pk>),
    path("", home, name='home'),
    path("search", search, name='search'),
    path("<slug>", detail, name='detail'),
]


