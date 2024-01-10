from rest_framework import serializers
from worker.models import ConcreteWorker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteWorker
        fields = "__all__"