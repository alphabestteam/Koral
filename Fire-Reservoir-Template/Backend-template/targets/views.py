from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer


@csrf_exempt
def add_target(request):
    #This function will add a target

    if request.method == 'POST':
        request_data = JSONParser().parse(request)

        target = Target(
            name=request_data["name"],
            attack_priority=request_data["attack_priority"],
            longitude=request_data["longitude"],
            latitude=request_data["latitude"],
            enemy_organization=request_data["enemy_organization"],
            target_goal=request_data["target_goal"],
            was_target_destroyed=request_data["was_target_destroyed"],
            target_id=request_data["target_id"]
        )

        serializer = TargetSerializer(data = request_data)
        if serializer.is_valid():
            target.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def update_target(request):
    # This function will update the target 

    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        print(request_data)
        id_number = request_data.get('target_id', None)
        target = Target.objects.get(target_id=id_number)
        serializer = TargetSerializer(target, data=request_data)

        if serializer.is_valid():
            target.name = request_data["name"]
            target.attack_priority = request_data["attack_priority"]
            target.longitude = request_data["longitude"]
            target.latitude = request_data["latitude"]
            target.enemy_organization = request_data["enemy_organization"]
            target.target_goal = request_data["target_goal"]
            target.was_target_destroyed = request_data["was_target_destroyed"]
            target.save()

            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


def all_targets(request):
    # This function will send all the targets

    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False)