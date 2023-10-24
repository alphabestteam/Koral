from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from books.models import Book, BookReview
from books.serializers import BookSerializer, BookReviewSerializer
import datetime
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view





@api_view(['POST'])
def add_book(request):
    # This function will add a new book to db 

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Book Added Successfully!", status=200)
    return HttpResponse("Error!", status=404)
    

@api_view(['PUT'])
def update_book(request, book_id):
    # This function will update the book fields in the db

    book = get_object_or_404(Book, book_id=book_id)

    serializer = BookSerializer(book, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Book Updated Successfully!", status=200)
    return HttpResponse(serializer.errors, status=400)


@api_view(['GET'])
def get_all_books(request):
    # This function will get all the books

    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['DELETE'])
def delete_book(request, book_id):
    # This function will delete a book

    book = get_object_or_404(Book, book_id=book_id)
    book.delete()
    return HttpResponse('book Deleted Successfully!', status=200)

        

@api_view(['POST'])
def add_book_review(request):
    # This function will add a description to the book

    serializer = BookReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Book Review Added Successfully!", status=200)
    return HttpResponse("Error!", status=404)
    
    

def calculate_how_many_years_from_published(book_id):
    # This function will calculate how much years from now the book got published

    instance = Book.objects.get(book_id=book_id)
    serializer = BookSerializer(instance)
    year_published = serializer.data['date_of_published'].year
    return datetime.now().year - year_published


def how_long_review_description(review_id):
    # This function will return the length of the review description

    instance = BookReview.objects.get(review_id=review_id)
    serializer = BookSerializer(instance)
    return len(serializer.data["review_description"])


"""
EX 2:
By using DRF serializers in the views, we can efficiently parse and validate data from incoming requests.


EX 3:
query_params are a way to pass additional data to a web sever via the URL , can be used with regex or just with sending variables. query parameters are used to filter, sort, or customize the data returned from the server. 

"""

def get_description(request, book_id):
    # This function will get the description of the desired book with its id 
    
    instance = Book.objects.get(book_id=book_id)
    serializer = BookSerializer(instance)
    return HttpResponse(serializer.data['description'])



"""
EX 4:

HttpResponse is used in Django for web applications, while Response is used in Django Rest Framework for building web APIs. They both represent HTTP responses but are used in different contexts.


EX 5:

Class-Based Views (CBVs) use classes to define views, which specialized in handling complex views and code reuse, which suitable for cases where you have multiple views sharing common functionality.
Function-Based Views (FBVs) use functions for view logic, which is simpler and straightforward fot basic views, which suitable for simple views that don't require extensive code reuse or shared behavior.

"""

class MyView(APIView):
    def get(self, book_id):
        # This function will return the name of the author of the book

        instance = Book.objects.get(book_id=book_id)
        serializer = BookSerializer(instance)
        return HttpResponse(serializer.data['author'])
    

"""
EX 6:

Using the "if" statement, you can get to some request.method , with *args and **kwargs variables, like the example below : 

FunctionView(request, *args, **kwargs):
    match request.method:
        case "GET":
            # do some stuff
            return response_for_get
        case "DELETE":
            # do some stuff
            return response_for_delete
        case "PATCH":
            # do some stuff
            return response_for_path
        case _: # post, put, option e.t.c
            # do some stuff
            return response_for_post

In this example we used the match-case statements in python to determinate the request method


EX 7:

The save() function in Django models determines whether to create a new object or update an existing one based on the value of the primary key field. If the object has a primary key value, it updates the existing object with the new data. If it doesn't, it creates a new object.


EX 8:

serializer.errors


EX 9:

The statement means that if the data that provided to the serializer is not valid, it will raise an exception , which means that the data has to be validated . its a good way from the usual way because it can provide a detailed error response to the client (if its a value error then return "You Entered A Wrong Value... or else)


EX 10:

In the serializers.py


EX 11:

using the "partial=True" field, we can perform partial updates , example: 
"""

@api_view(['PUT'])
def update_book_name(request, book_id):
    # This function will update the book name to the desired book by its id

    book = book.objects.get(book_id=book_id)
    serializer = BookSerializer(book, data=request.dat, partial=True)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("The Book Name Got Updated!", status=200)
    return HttpResponse(serializer.errors, status=400)

"""
EX 12:

The depth option,in Meta class, controls the depth of serialization when dealing with nested relationships, which determines how many levels of related objects should be included when serializing data, which allowing to balance between detailed data and performance. For example, depth=1 will include the immediate related objects, bit depth=2 will include the immediate related objects and the related objects one level deeper.


EX 13:

In serializers.py lines 15-18


EX 14: 

The ReadOnlyField is a field that is displayed but you can't change it, which means that field can't be used to update or create objects.
example in serializers, in lines 21 - 26


EX 15:

SerializerMethodField is a read only field, but in this field you can define the value of the field by calculating the value, which makes the value more dynamic and costumed.
example in serializers, in lines 32 - 35


EX 16: 

SlugRelatedField is used to represent related objects in a serialized form, using a unique slug field from the related model instead of its primary key.
In SlugRelatedField, read_only=True means that the field is used for displaying related data in the serialized output, but it can't be used to update or create objects. It's read-only in terms of client interaction. 

example, 

models.py : 
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
serializers.py:
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Product
        fields = ['name', 'category']


EX 17: 

select_related is used for reducing database queries involving foreign key and one-to-one relationships by fetching related objects in a single query. you use select_related when you need related object data immediately.
prefetch_related is reduces database queries for many-to-many and reverse foreign key relationships by fetching related objects in a separate query. you use prefetch_related when you have many related objects and don't need them right away.

for example, 
if i want the author from book id number 1: 

book = Book.objects.select_related('author').get(id=1)

lets say i have 2 separate models, Genre ('name' field) and Book ('title' and 'genres' fields), if i want to retrieve a book and its associated genres: 
book = Book.objects.prefetch_related('genres').get(id=1)


EX 18:

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'timestamp']  # Include all the message fields you need

class UserSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'messages']

"""




    