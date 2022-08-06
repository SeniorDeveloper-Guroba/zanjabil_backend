from django.urls import path, include
from . import views
from .views import *
from .delivery import *

urlpatterns = [
    # path('', views.index, name='index'),
    path('address', AddressAPIView.as_view()),
    path('restaurant', RestaurantAPIView.as_view()),
    path('price', DeliveryPrice.as_view()),

    # path('menu', RestaurantAPIView.as_view()),
]