from django.db import models
from chat.models import Chat


class Message(models.Model):
    text = models.TextField(max_length=1000)
    sending_date = models.DateField()
    chat_pointer = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_sender = models.ForeignKey(to='users.User', null=False, on_delete=models.CASCADE)
    user_to_send = models.ManyToManyField(to='users.User', related_name="user_to_send")
    is_read = models.BooleanField(default=False, editable=False)
    message_id = models.AutoField(primary_key=True)

    
