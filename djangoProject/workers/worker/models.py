from django.db import models

GENDER_CHOICES = (
    ("female", "female"),
    ("male", "male"),
    ("other", "other")
)

class Worker(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    salary = models.IntegerField()
    gender = models.CharField(max_length = 60, choices = GENDER_CHOICES, default = GENDER_CHOICES[0])

    class Meta:
        abstract = True


class ConcreteWorker(Worker):
    class Meta:
        db_table = 'Worker'  
