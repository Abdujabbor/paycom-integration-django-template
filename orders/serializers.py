from .models import Order
from rest_framework import serializers
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('product_ids', 'amount', 'user_id', 'phone')