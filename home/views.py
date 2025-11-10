from django.shortcuts import render
from home.models import SettingSite
from post.models import Post
from category.models import Category


# Create your views here.
def home(request):
    posts   = Post.objects.all()[:12]
    posts_s = Post.objects.filter(slider=True).order_by('-created')[:4]

    return render(request, 'home/home.html', {'posts':posts, 'posts_s':posts_s})
