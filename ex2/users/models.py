from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    id_number = models.IntegerField(primary_key=True, validators=[MinValueValidator(111111111), MaxValueValidator(999999999)])
    email = models.EmailField()
    unread_messages = models.ManyToManyField(to='message.Message', related_name="unread_messages", blank=True, editable=False)

    