from rest_framework import serializers
from .models import *



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
        