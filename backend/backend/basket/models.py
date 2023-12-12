from django.db import models
from user.models import User
from product.models import Product


class Category(models.Model):
    user_id = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    basket_id = models.AutoField(primary_key = True)
    number_of_products = models.IntegerField()
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits = 1000, decimal_places = 2 )