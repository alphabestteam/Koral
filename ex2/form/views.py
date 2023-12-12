from form.models import FileSharingForm, Form, MessagesForm 
from form.serializers import FormSerializer, MessagesFormSerializer, FileSharingFormSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FileSharingViewSet(viewsets.ModelViewSet):
    queryset = FileSharingForm.objects.all()
    serializer_class = FileSharingFormSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = MessagesForm.objects.all()
    serializer_class = MessagesFormSerializer


