from django.urls import path
from .views import post_page, all_post, search, add_post

app_name = 'post'
urlpatterns = [
    path('', all_post, name='blog-home'),
    path('post/<int:pk>', post_page, name='post_page'),
    path('post/add', add_post, name='add_post'),
    path('search/', search, name='search'),

]