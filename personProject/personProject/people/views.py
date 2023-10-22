from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


from people.models import Person, Parent
from people.serializers import PersonSerializer, ParentSerializer
from datetime import date

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

"""

PARENTS AREA!
NOT FOR UNDER 18!

"""


@csrf_exempt
def get_all_parents(request):
    # This function returns all of the parents

    if request.method == "GET":
       parents = Parent.objects.all()
       return HttpResponse(parents, status=200)


@csrf_exempt
def add_parent(request):
    # This function adds a parent

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ParentSerializer(data=data)
        if serializer.is_valid():

            parent = Parent(
                name = data["name"],
                date_of_birth = data["date_of_birth"],
                city = data["city"],
                id_number = data["id_number"],
                work_place = data["work_place"],
                base_salary = data["base_salary"]
            )

            parent.save()
            parent.children.set(data.get('children', []))
            return JsonResponse('Person Added Successfully!', status=200, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)

#http://127.0.0.1:8000/people/api/addPerson/


@csrf_exempt
def remove_parent(request, id_number):
    # This function removes a parent with the given id number

    if request.method == "DELETE":
        try:
            parent = Parent.objects.get(id_number=id_number)
            parent.delete()
            return HttpResponse('Parent Deleted!', status=200)
        except:
            raise HttpResponse(status=404)

    
@csrf_exempt
def update_parent(request):
    # This function will update the Parent

    if request.method == "POST":
        data = JSONParser().parse(request)
        parent = Parent.objects.get(id_number=data["id_number"])
        serializer = ParentSerializer(parent, data)
        if serializer.is_valid():
            serializer.update(parent, data)
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(status=404)
        

@csrf_exempt
def connect_child(request):
    # This function will connect the child to it's parent

    if request.method == "POST":
        try:
            id_dict = JSONParser().parse(request)
            parent_id = Parent.objects.get( id = id_dict["parent_id"])
            child_id = Person.objects.get( id = id_dict["child_id"])
            if child_id not in parent_id.children.all(): # checking if the id of the kid is in the list of children in the current parent
                parent_id.children.add(child_id)
                return HttpResponse('Connected Successfully!', status=200)
            return HttpResponse('The Child Is Already In The List Of The Parent', status=404)
        except:
            return HttpResponse('Error!', status=404)
        

@csrf_exempt
def parent_info(request, id_number):
    # This function will print the info of the desired parent

    if request.method == "GET": 
        try:
            parent = Parent.objects.get(id_number=id_number)
            return HttpResponse('The Parent Info : \n', parent, status=200)
        except:
            return HttpResponse('Error!', status=404)
        

@csrf_exempt
def rich_children(request):
    # This function will print a list of all the info of the rich kids, which one of his parents salary is more then 50,000 and his kid is under 18 years old

    if request.method == "GET":

        rich_children = []
        parent_with_rich_children = Parent.objects.filter(base_salary__gt=50000.00)

        for parent in parent_with_rich_children:
            check_rich_children = parent.children.all()
            for child in check_rich_children:
                child_age = date.today().year - child.date_of_birth.year
                if child_age > 18:
                    child_serialized = PersonSerializer(child)
                    rich_children.append(child_serialized.data)

        if not rich_children:
            return HttpResponse('No Rich Children', status=404)
        
        return HttpResponse(rich_children, status=200)
    

@csrf_exempt
def parents_names(request, id_number):
    # This function will return the names of the parents of the desired childs id number

    if request.method == "GET":
        parents_list = []
        
        parents = Parent.objects.all()
        for parent in parents.all():
            for child in parent.children.all():
                if int(id_number) == int(child.id_number):
                    parents_list.append(parent)
        
        if not parents_list:
            return HttpResponse("No Parents Found!", status=404)
        return HttpResponse(parents_list, status=200)
    


@csrf_exempt
def children_information(request, id_number):
    # This function will return the information of the children of the desired parents id number

    if request.method == "GET":
        try:
            parent = Parent.objects.get(id_number = id_number)
            children = parent.children.all()
            children_serializer = PersonSerializer(children, many=True)
            child_data = children_serializer.data

            return JsonResponse(child_data, status=200, safe=False)
        except:
            return JsonResponse('Parent Could Not Be Found', status = 404)


@csrf_exempt
def grandparents_information(request, id_number):
    # This function will return the information of the grandparents of the desired grandchild id number

    if request.method == "GET":
        grandparents =[]

        try:
            grandchild = Person.objects.get(id_number=id_number)
        except:
            return HttpResponse("Wrong Id Number!", status=400)
    
        parents = grandchild.parents.all()
        for parent in parents:
            grandparents.append(parent.parents.all())
        
        if not grandparents:
            return HttpResponse("No Grandparents Found!", status=404)
        return HttpResponse(grandparents, status=200)


@csrf_exempt
def brothers_information(request, id_number):
    # This function will return the information of the brothers of the desired person id number

    if request.method == "GET":
        brothers = []

        try:
            person = Person.objects.get(id_number=id_number)
        except:
            return HttpResponse("Wrong Id Number!", status=400)

        parents = person.parents.all()
        for parent in parents:
            brothers.append(parent.children.all())

        if not brothers:
            return HttpResponse("No Brothers Found!", status=404)
        return HttpResponse(brothers, status=200)
