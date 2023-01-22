from datetime import datetime

from django.db import models

# Create your models here.
class AddressModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=6, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=6, null=True)
    isDefault = models.BooleanField(default=False, null=True)
    intercom = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    build = models.CharField(max_length=255, null=True)
    apartment = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Address'

class MenuCategoryModel(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, default="", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menu categories'

class DishModel(models.Model):
    name = models.CharField(max_length=255, default=None)
    preview = models.CharField(max_length=50, default=None, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    description = models.CharField(max_length=255, default=None, null=True)
    menu_category = models.ForeignKey(MenuCategoryModel, on_delete=models.CASCADE, null=True)
    #menu_category = models.ForeignKey('zanjabil_backend.MenuCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dish'

class MenuModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menu'

class RestaurantModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True)
    menu_id = models.ForeignKey(MenuModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Restaurant'

class UserModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     totalPrice = models.IntegerField()
#     dateCreate = models.DateTimeField()
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

