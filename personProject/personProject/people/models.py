from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.IntegerField(primary_key=True, validators=(MinValueValidator(111111111),MaxValueValidator(999999999)))
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'The name is: {self.name}\nThe id is: {self.id_number}\nThe date of birth is: {self.date_of_birth}\nThe city is: {self.city}'

# Create your models here.
