from django.shortcuts import render
from UserApp.models import *
from UserApp.serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password
from Jetronics.validation import Validate
import json
from rest_framework import status
import datetime
from Jetronics.pagination import Mypagination
from ProductApp.models import *
from ProductApp.serializers import *
from StatusApp.models import *
from StatusApp.serializers import *
from OrderApp.models import *
from OrderApp.serializers import *
