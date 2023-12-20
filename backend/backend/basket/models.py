from django.db import models

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Basket(models.Model):
    user_id = models.ForeignKey(to="user.User", null = True, on_delete = models.CASCADE)
    basket_id = models.AutoField(primary_key = True)
    number_of_products = models.IntegerField(validators = [MinValueValidator(1)],default=0)
    product = models.ManyToManyField(to = "product.Product", related_name="productsList")
    total_price = models.DecimalField(
        validators=[MinValueValidator(0)], 
        default=0.00, 
        max_digits=10, 
        decimal_places=2  
          )

