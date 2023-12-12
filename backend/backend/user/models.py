from django.db import models
from product.models import Product
from basket.models import Basket

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    shopping_history = models.ForeignKey(Basket, null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)