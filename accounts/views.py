from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from post.models import Post


# Create your views here.
def login_site(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == "POST":
        number   = request.POST.get("number")
        password = request.POST.get("password")

        user     = authenticate(request, number=number, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            return render(request, "accounts/login.html", {'message': 'Invalid username or password.'})


    return render(request, 'accounts/login.html')

def logout_site(request):
    logout(request)
    return redirect('home:home')

def signup_site(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == "POST":
        number     = request.POST.get("number")
        first_name = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        password   = request.POST.get("password")

        if User.objects.filter(number=number).exists():
            return render(request, "accounts/signup.html", {'message': 'number already registered.'})

        user = User.objects.create_user(number=number, password=password, first_name=first_name, last_name=last_name)

        login(request, user)

        return redirect('home:home')
    else:
        return render(request, "accounts/signup.html")

    return render(request, "accounts/signup.html")

def writer(request, user_name):
    user  = User.objects.get(username=user_name)
    posts = Post.objects.filter(writer=user)

    return render(request, 'accounts/author.html', {'posts': posts, 'user': user})

def profile(request, pk):
    if not request.user.is_authenticated and not request.user.id == pk:
        return redirect('home:home')

    user = User.objects.get(id=pk)
    if not request.method == "POST":
        return render(request, 'accounts/profile.html', {'user': user})

    messages = dict()
    if request.POST.get("username") != user.username and User.objects.filter(username=request.POST.get("username")).exists():
        messages['username_message'] =  'username already in use.'
    else:
        user.username = request.POST.get("username")

    if request.POST.get("email") != user.email and User.objects.filter(email=request.POST.get("email")).exists():
        messages['email_message'] = 'email already in use.'
    else:
        user.email = request.POST.get("email")

    if request.POST.get("number") != user.number and User.objects.filter(number=request.POST.get("number")).exists():
        messages['number_message'] = 'number already in use.'
    else:
        user.number = request.POST.get("number")

    user.first_name = request.POST.get("first_name")
    user.last_name = request.POST.get("last_name")
    user.bio = request.POST.get("bio")
    if request.FILES.get("picture"):
        user.picture = request.FILES.get("picture")
    user.save()

    if messages:
        return render(request, 'accounts/profile.html', {'user': user, 'messages': messages})


    return render(request, 'accounts/profile.html', {'user': user})