from abc import ABC
from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.Serializer):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class AddressSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    longitude = serializers.DecimalField(max_digits=20, decimal_places=6)
    latitude = serializers.DecimalField(max_digits=20, decimal_places=6)
    isDefault = serializers.BooleanField(read_only=True)
    intercom = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    build = serializers.CharField(max_length=255)
    apartment = serializers.CharField(max_length=255)


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategoryModel
        fields = ('name', 'dishes', 'icon')
