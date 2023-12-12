from users.models import User 
from users.serializers import UserSerializer
from message.models import Message
from message.serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @api_view(['GET'])
    def unread_messages(self, user_id):
        user = User.objects.get(pk=user_id)
        unread_messages = Message.objects.filter(chat_pointer__user_receiver=user, is_read=False)
        serializer = self.get_serializer(unread_messages, many=True)
        return Response(serializer.data, status=200)