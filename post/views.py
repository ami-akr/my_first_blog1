from accounts.views import User
from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from post.models import Post, Comment
from django.core.paginator import Paginator


# Create your views here.
def all_post(request):
    posts_list = Post.objects.order_by('-created')
    last_post  = Post.objects.order_by('-created')[4:8]
    categories = Category.objects.all()[:10]
    page       = request.GET.get('page', 1)
    paginator  = Paginator(posts_list, 10)
    posts      = paginator.get_page(page)


    return render(request, 'post/blog.html', {'posts': posts, 'last_post': last_post, 'categories': categories})

def post_page(request, pk):
    post = get_object_or_404(Post, id=pk)
    post_before = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    post_after = Post.objects.filter(id__gt=post.id).order_by('id').first()

    if request.user.is_authenticated and not post.has_seen(request.user):
        post.views.add(request.user)
        post.save()

    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST.get('message')
            user    = User.objects.get(id=request.user.id)
            Comment.objects.create(user=user, post=post, body=message)
        else:
            return redirect('accounts:login')

    return render(request, 'post/post_page.html', {'post': post, 'post_before': post_before, 'post_after': post_after})

def search(request):
    query      = request.GET.get('q')
    post_list  = Post.objects.filter(title__icontains=query).order_by('-created')
    paginator  = Paginator(post_list, 5)
    page       = request.GET.get('page', 1)
    posts      = paginator.get_page(page)
    last_post  = Post.objects.order_by('-created')[4:8]
    categories = Category.objects.all()[:10]

    return render(request, 'post/blog.html', {'posts': posts, 'last_post': last_post, 'categories': categories})

def add_post(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if not request.method == 'POST':
        categories = Category.objects.all()
        return render(request, 'post/add_post.html', {'categories': categories})

    title = request.POST.get('title')
    body  = request.POST.get('body')
    image = request.FILES.get('image')
    post  = Post.objects.create(title=title, body=body, image=image, writer=request.user, slider=True)
    return redirect('post:post_page', pk=post.id)