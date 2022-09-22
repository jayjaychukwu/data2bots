from accounts.serializers import UserSerializer
from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    client = UserSerializer()

    class Meta:
        model = Order
        fields = "__all__"
