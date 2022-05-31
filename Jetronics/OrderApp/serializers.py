from rest_framework import serializers
from ProductApp.serializers import ProductSerializer

from StatusApp.serializers import StatusSerializer
from .models import *
from StatusApp.models import *



class OrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = '__all__'

    def get_status(self,obj):
        

        v_obj = StatusModel.objects.filter(statuscode=obj.status.statuscode)
        v_qs = StatusSerializer(v_obj, many=True)
        
        return v_qs.data


class MultipleorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('id','phone','userrandomid')


class MissingOrderSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = MissingOrder
        fields = '__all__'

    
    def get_product(self,obj):
        v_obj = ProductModel.objects.filter(id=obj.product.id)
        v_qs = ProductSerializer(v_obj, many=True)
        
        return v_qs.data
