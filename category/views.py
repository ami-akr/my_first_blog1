from django.core.paginator import Paginator
from django.shortcuts import render
from category.models import Category
from post.models import Post


# Create your views here.
def category(request, title):
    category   = Category.objects.get(title=title)
    posts_list      = category.posts.all()
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('q')
    posts = paginator.get_page(page)
    lasts_post = category.posts.order_by('-id')[:3]

    return render(request,'category/category_page.html', {'category':category, 'posts':posts, 'lasts_post':lasts_post})

