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
    type = models.CharField(choices = TYPE_CHOICES, max_length = 50)
    gender = models.CharField(choices = GENDER_CHOICES, default = "OTHER", max_length = 50)
    season = models.CharField(choices = SEASON_CHOICES, max_length = 50)
    collection = models.CharField(choices = COLLECTIONS_CHOICES, default = "CASUAL", max_length = 50)
    
    def __str__(self):
        return f"{self.get_collection_display()} - {self.get_type_display()} - {self.get_gender_display()} - {self.get_season_display()}"