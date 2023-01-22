from rest_framework import generics
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import *
from apps.zanjabil_backend.serializers import *


# def index(request):
#     text = ""
#     address = {}
#     a = Address.objects.get(id=1)
#     address["name"]      = a.name
#     address["street"]    = a.street
#     address["build"]     = a.build
#     address["city"]      = a.city
#     address["apartment"] = a.apartment
#     return JsonResponse(address)
#
# def getRestaurants(request):
#     restaurant = Restaurant.objects.get(id=1)
#     sendRestaurant = {}
#     sendRestaurant["name"] = restaurant.name
#     sendRestaurant["description"] = restaurant.description
#     sendRestaurant["address"] = restaurant.address
#     sendRestaurant["menu"] = restaurant.menu
#     return JsonResponse(sendRestaurant)


class RestaurantAPIView(generics.ListAPIView):
    def get(self, request):
        #
        addressModel = AddressModel.objects.get(id=3)
        addressSerializer = AddressSerializer(addressModel)
        address = JSONRenderer().render(addressSerializer.data)
        #
        menuObject = MenuModel.objects.get(id=1)
        menuCategories = MenuCategoryModel.objects.all().values()
        dishes = DishModel.objects.all().values()
        menu = {}
        menu["name"] = menuObject.name
        menu["categories"] = menuCategories
        menu["dishes"] = dishes
        #
        restaurantObject = RestaurantModel.objects.get(id=1)
        restaurant = {}
        restaurant["name"] = restaurantObject.name
        restaurant["description"] = restaurantObject.description
        restaurant["menu"] = menu
        restaurant["address"] = addressSerializer.data
        return Response(restaurant)

    # model_to_dict
    # def get(self, request):
    #     restaurant = Restaurant.objects.get(id=1)
    #     sendRestaurant = {}
    #     sendRestaurant["name"] = restaurant.name
    #     sendRestaurant["description"] = restaurant.description
    #     sendRestaurant["address"] = restaurant.address
    #     sendRestaurant["menu"] = restaurant.menu
    #     return JsonResponse(sendRestaurant)

    # queryset = Restaurant.objects.all()
    # serializer_class = RestaurantSerializer
    # restaurant = Restaurant.objects.all().values()
