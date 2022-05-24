from django.urls import path
from .views import *

urlpatterns = [
    path('UserView/',UserView.as_view()),
    path('Login/',LoginView.as_view()),
    path('User/',LoginedUser.as_view()),
    path('Logout/',LogoutView.as_view()),
]