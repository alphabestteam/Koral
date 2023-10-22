from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Target(models.Model):
    name = models.CharField(max_length=100)
    attack_priority = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    longitude = models.DecimalField(decimal_places=4, max_digits=1000)
    latitude = models.DecimalField(decimal_places=4, max_digits=1000)
    enemy_organization = models.CharField(max_length=100)
    target_goal = models.CharField(max_length=100)
    was_target_destroyed = models.BooleanField()
    target_id = models.IntegerField(MinValueValidator(0), primary_key=True)

    def __str__(self):
        return self