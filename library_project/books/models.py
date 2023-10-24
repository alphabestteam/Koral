from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    pages_count = models.IntegerField()
    genre = models.CharField(max_length=20)
    date_of_published = models.DateField()



class BookReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    author =  models.CharField(max_length=50)
    review_description = models.CharField(max_length=200)
