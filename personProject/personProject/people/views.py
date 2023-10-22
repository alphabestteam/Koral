from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from people.models import Person
from people.serializers import PersonSerializer


@csrf_exempt
def get_all_people(request):
    # This function returns all of the person

    if request.method == "GET":
       person = Person.objects.all()
       return HttpResponse(person, status=200)


@csrf_exempt
def add_person(request):
    # This function adds a person

    if request.method == "POST":
        data = JSONParser().parse(request)

        person = Person(
            name = data["name"],
            date_of_birth = data["date_of_birth"],
            city = data["city"],
            id_number = data["id_number"]
        )

        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            person.save()
            return JsonResponse('Person Added Successfully!', status=200, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

#http://127.0.0.1:8000/people/api/addPerson/


@csrf_exempt
def remove_person(request, id_number):
    # This function removes a person with the given id number

    if request.method == "DELETE":
        try:
            person = Person.objects.get(id_number=id_number)
            person.delete()
            return HttpResponse('Person Deleted!', status=200)
        except:
            raise HttpResponse(status=404)

    
@csrf_exempt
def update_person(request):
    # This function will update the person

    if request.method == "POST":
        data = JSONParser().parse(request)
        person = Person.objects.get(id_number=data["id_number"])
        serializer = PersonSerializer(person, data)
        if serializer.is_valid():
            serializer.update(person, data)
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(status=404)


