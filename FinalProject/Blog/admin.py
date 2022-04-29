from django.contrib import admin
from Blog.models import Author, post, Category

admin.site.register(Author)
admin.site.register(post)
admin.site.register(Category)

