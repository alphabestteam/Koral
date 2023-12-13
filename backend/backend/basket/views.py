from basket.models import Basket
from django.db.models.signals import post_save
from django.dispatch import receiver

from basket.serializers import BasketSerializer

from rest_framework import viewsets


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

