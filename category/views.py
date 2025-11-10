from django.shortcuts import render
from category.models import Category
from post.models import Post


# Create your views here.
def category(request, title):
    category   = Category.objects.get(title=title)
    posts      = category.posts.all()
    lasts_post = category.posts.order_by('-id')[:3]

    return render(request,'category/category_page.html', {'category':category, 'posts':posts, 'lasts_post':lasts_post})

