from django.db import models
from category.models import Category

STATUS_CHOICES = (
    ("OUT_OF_STOCK", "out of stock"),
    ("NOT_AVAILABLE", "not available"),
    ("IN_STOCK", "in stock")
)


class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    price = models.DecimalField(decimal_places = 2,max_digits = 1000)
    status = models.CharField(choices = STATUS_CHOICES, default = "IN_STOCK", max_length=80)
    picture = models.ImageField()
    category = models.ManyToManyField(Category, related_name="category")


    def __str__(self) -> str:
        return f"{self.name} - {self.price}$"