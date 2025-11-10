from django.urls import path
from .views import category


urlpatterns = [
    path('<str:title>/', category, name='category'),
]