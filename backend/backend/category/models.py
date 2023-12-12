from django.db import models

TYPE_CHOICES = (
    ("SHIRT", "shirt"),
    ("PANTS", "pants"),
    ("DRESS", "dress"),
    ("SPORT_BRA", "sport bra"),
    ("TIGHTS", "tights"),
    ("SHOES", "shoes")
)

GENDER_CHOICES = (
    ("FEMALE", "female"),
    ("MALE", "male"),
    ("KIDS", "kids")
)

SEASON_CHOICES = (
    ("SUMMER", "summer"),
    ("FALL", "fall"),
    ("WINTER", "winter"),
    ("SPRING", "spring")
)

COLLECTIONS_CHOICES = (
    ("SPORTSWEAR", "sportswear"),
    ("EVENING", "evening"),
    ("CASUAL", "casual"),
)


class Category(models.Model):
    id = models.AutoField(primary_key = True)
    type = models.CharField(choices = TYPE_CHOICES)
    gender = models.CharField(choices = GENDER_CHOICES, default="OTHER")
    season = models.CharField(choices = SEASON_CHOICES)
    collection = models.CharField(choices = COLLECTIONS_CHOICES, default = "CASUAL")
    
