from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class user_registration(models.Model):
    user_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    screen_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="Blog/media")

    def __str__(self):
     return self.user.name

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length =100)
    subtitle = models.CharField(max_length=50)
    img = models.ImageField(upload_to ='post_images', null=True, blank=True)
    post = models.TextField()
    categories = models.ManyToManyField(Category)
