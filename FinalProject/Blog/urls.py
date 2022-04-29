from msilib.schema import Icon
from django.contrib import admin
from django.urls import path
from Blog.views import *


urlpatterns = [
    path('', home, name= "home"),
    path('user_registration/', user_registration, name= "Registration"),
    path('create_post/', create_post, name= "Create Post"),
    path('user_login/', user_login, name= "Login"), 
    path('pages', post_view, name="Post"),
    path('page detail/<id>', page_detail, name= "Page detail"),
    path('about/', about, name= "About"),
    path('Tutorials/', Tutorials, name="Tutorials"),
    path('Links/', Links, name="Links"),
]
