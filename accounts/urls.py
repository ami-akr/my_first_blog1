import profile

from django.contrib.auth import logout
from django.urls import path
from .views import login_site, signup_site, logout_site, writer, profile

app_name = 'accounts'
urlpatterns = [
    path('login/', login_site, name='login'),
    path('logout/', logout_site, name='logout'),
    path('signup/', signup_site, name='signup'),
    path('writer/<str:user_name>', writer, name='writer'),
    path('user/<int:pk>', profile, name='profile'),
]