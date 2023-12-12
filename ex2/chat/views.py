from chat.models import Chat
from chat.serializers import ChatSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

