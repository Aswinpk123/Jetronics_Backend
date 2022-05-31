from xml.etree.ElementInclude import include
from rest_framework import serializers
from .models import *
from Jetronics.pagination import Mypagination

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class MoreProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreProductImage
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    productimage = serializers.SerializerMethodField()
   
    class Meta:
        model = ProductModel
        fields = '__all__'


    def get_productimage(self,obj):
    
        v_obj = MoreProductImage.objects.filter(image_id=obj.id)
        v_qs = MoreProductImageSerializer(v_obj, many=True)
        
        return v_qs.data


class ProductSerializeruserView(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


