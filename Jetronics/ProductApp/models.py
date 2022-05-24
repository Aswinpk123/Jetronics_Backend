from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    description = models.CharField(max_length=255,null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class MoreProductImage(models.Model):
    image_id = models.CharField(max_length=255,blank=False,null=False)
    productimage = models.ImageField(upload_to='MoreImage',blank = True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class ProductModel(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    brand = models.CharField(max_length=255,null=False,blank=False)
    title = models.CharField(max_length=255,null=False,blank=False)
    code = models.CharField(max_length=255,null=False,blank=False)
    purchase_price = models.CharField(max_length=255,null=True,blank=True)
    price = models.CharField(max_length=255,null=False,blank=False)
    offer_price = models.CharField(max_length=255,null=True,blank=True)
    deliverycharge = models.CharField(max_length=255,blank=True,null=True,default=0)
    size = models.CharField(max_length=255,null=True,blank=True)
    colour = models.CharField(max_length=255,null=True,blank=True)
    quantity = models.CharField(max_length=255,null=False,blank=False)
    fake_order_sold = models.CharField(max_length=255,null=True,blank=True)
    rank = models.CharField(max_length=255,null=False,blank=False)
    description = models.CharField(max_length=255,null=False,blank=False)
    status = models.CharField(max_length=255,null=False,blank=False)
    product_image = models.ImageField(upload_to='ProductImage',blank = False,null=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    
