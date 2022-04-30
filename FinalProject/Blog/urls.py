from django.urls import path
from Blog.views import *

urlpatterns = [
    path('', home, name= "home"),
    path('create_post/', create_post, name= "Create Post"),
    path('pages', post_view, name="Post"),
    path('page detail/<id>', page_detail, name= "Page detail"),
    path('update-post/<id>', update_post, name="Update post"),
    path('remove-post/<id>', remove_post, name="Remove post"),
    path('about/', about, name= "About"),
    path('Tutorials/', Tutorials, name="Tutorials"),
    path('Links/', Links, name="Links"),
    path('chat', chat, name="Chat")
]
