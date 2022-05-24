from django.db import models

# Create your models here.

class StatusModel(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    description = models.CharField(max_length=255,null=True,blank=True)
    colour = models.CharField(max_length=255,null=False,blank=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)