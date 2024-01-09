from worker.models import Worker
from worker.serializers import WorkerSerializer

from rest_framework import viewsets

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


    """
      to get all the list of workers and also to add a new worker :
        http://127.0.0.1:8000/workers/api/
      to  update / delete a specific user : 
        http://127.0.0.1:8000/workers/api/<users_id>/


    """

