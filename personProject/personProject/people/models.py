from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.IntegerField(primary_key=True, validators=(MinValueValidator(111111111),MaxValueValidator(999999999)))
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'The name is: {self.name}\nThe id is: {self.id_number}\nThe date of birth is: {self.date_of_birth}\nThe city is: {self.city}'


class Parent(Person):
    work_place = models.CharField(max_length=100)
    base_salary = models.DecimalField(decimal_places=2, max_digits=8)
    children = models.ManyToManyField(Person, related_name='parents', blank = True)

    def __str__(self) -> str:
        return f'The parent name is: {self.name}\n The id is: {self.id_number}\n The date of birth is: {self.date_of_birth}\n The city is: {self.city}\n The place of work is: {self.place_of_work}\n The base salary is: {self.salary}\n The children are: {self.children.all().values()}'