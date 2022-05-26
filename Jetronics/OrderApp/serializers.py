from rest_framework import serializers
from .models import *

class MissingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'