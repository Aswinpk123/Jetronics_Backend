from django.urls import path
from .views import *


urlpatterns = [
    path('missingorder/',MissingOrderView.as_view()),
    path('allorder/',OrderViews.as_view()),
]