from django.urls import re_path
from. import views

urlpatterns = [
    re_path(r'^posts/$', views.BlogPost.as_view(), name= 'posts'),
    #re_path(r'^posts/?p<pk>)
]
