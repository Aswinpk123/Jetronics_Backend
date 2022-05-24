from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserDetailsModel(AbstractUser):
    mobile = models.CharField(max_length=100,blank=True)
    address = models.TextField(max_length=100,blank=True)
    gender = models.CharField(max_length=100,blank=True)
    dob = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    prof_image = models.ImageField(upload_to='ProfileImage',blank=True)

