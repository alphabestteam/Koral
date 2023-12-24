from django.db import models
from basket.models import Basket

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    shopping_history = models.ManyToManyField(Basket, related_name='shoppers', editable=False)


    # def __str__(self) -> str:
    #     return self.username