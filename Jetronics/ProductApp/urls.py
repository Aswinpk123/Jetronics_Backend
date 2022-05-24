from django.urls import path
from .views import *

urlpatterns = [

    path('category/',ProductCategoryViewAdmin.as_view()),
    path('categoryall/',ProductCategoryViewalluser.as_view()),
    path('product/',ProductView.as_view()),
    path('moreimages/',MoreImageView.as_view()),
    path('statuschange/',StatusUpdateView.as_view()),
]