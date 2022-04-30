from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length =100)
    subtitle = models.CharField(max_length=50)
    img = models.ImageField(upload_to ='post_images', null=True, blank=True)
    post = models.TextField()

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    chat = models.CharField(max_length=400)
    def __str__(self):
        return f"id: {self.id}, user: {self.user}, chat: {self.chat}"
