from message.models import Message
from message.serializers import MessageSerializer

from users.models import User
from users.serializers import UserSerializer

from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class SendMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @api_view(['POST'])
    def send_message(self, request):
        message_id = Message.objects.get('message_id')
        user_to_send_id = request.data.get('user_to_send')

        message = get_object_or_404(Message, pk=message_id)
        user_to_send = get_object_or_404(User, id_number=user_to_send_id)

        message.chat_pointer.save()
        message.save()

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=200)


    