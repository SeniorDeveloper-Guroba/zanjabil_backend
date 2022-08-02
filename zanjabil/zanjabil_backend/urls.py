from django.urls import path, include
from . import views
from .views import RestaurantAPIView

urlpatterns = [
    # path('', views.index, name='index'),
    path('restaurants', RestaurantAPIView.as_view()),
    path('restaurant', RestaurantAPIView.as_view()),
    # path('menu', RestaurantAPIView.as_view()),
]