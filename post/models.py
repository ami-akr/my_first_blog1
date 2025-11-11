from django.db import models

import post
from accounts.models import User
from category.models import Category
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=150)
    category    = models.ManyToManyField(Category, related_name='posts', blank=True)
    body        = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    writer      = models.ForeignKey(User, on_delete=models.CASCADE)
    views       = models.ManyToManyField(User, related_name='users_views', blank=True)
    image       = models.ImageField(upload_to='post/images/')
    slider      = models.BooleanField(default=False)

    def linkpost(self):
        return reverse('post:post_page', kwargs={'pk':self.id})

    def has_seen(self, user):
        return self.views.filter(id=user.id).exists()

    def __str__(self):
        return f"{self.title[:30]}...-{self.created}"

class Comment(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body    = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return f"{self.body[:30]}..."
