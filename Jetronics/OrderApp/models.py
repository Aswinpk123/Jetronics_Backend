from django.db import models
from ProductApp.models import *

# Create your models here.

class MissingOrder(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    clientname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class OrderModel (models.Model):
    product_id = models.CharField(max_length=255,default='')
    userrandomid = models.CharField(max_length=255,default='')
    orderid = models.CharField(max_length=255)
    clientname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    address = models.CharField(max_length=255,default='')
    product_code = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    deliverycharge = models.CharField(max_length=255)
    product_VAT = models.CharField(max_length=255)
    product_total = models.CharField(max_length=255)
    product_size = models.CharField(max_length=255,null=True,blank=True)
    product_colour = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255,default='')
    product_image_url = models.CharField(max_length=255,default='')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class OrderSettingsModel(models.Model):
    key = models.CharField(max_length=255,default=1)
    value = models.CharField(max_length=255)