from django.urls import path
from .views import *


urlpatterns = [
   path('status/',StatusView.as_view())
]