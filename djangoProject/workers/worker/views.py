from django.shortcuts import get_object_or_404
from worker.models import ConcreteWorker
from rest_framework.decorators import api_view
from rest_framework.response import Response
from worker.serializers import WorkerSerializer


@api_view(['GET'])
def get_workers(request):
    # This function will return a list of all the workers

    ConcreteWorkers = ConcreteWorker.objects.all()
    serializer = WorkerSerializer(ConcreteWorkers, many=True)
    return Response({'workers': serializer.data})


@api_view(['POST'])
def add_worker(request):
    # This function will add a worker

    serializer = WorkerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_worker(request, worker_id):
    # This function will update the worker with the given id 

    worker = get_object_or_404(ConcreteWorker, id=worker_id)
    serializer = WorkerSerializer(worker, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_worker(request, worker_id):
    # This function will delete a worker with the given id 

    worker = get_object_or_404(ConcreteWorker, id=worker_id)
    worker.delete()
    return Response({f'Worker Deleted Successfully !'})