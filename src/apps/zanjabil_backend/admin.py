from django.contrib import admin

# Register your models here
from .models import *

admin.site.register(RestaurantModel)
admin.site.register(AddressModel)
admin.site.register(MenuModel)
admin.site.register(DishModel)
admin.site.register(MenuCategoryModel)
# admin.site.register(User)
# admin.site.register(Order)