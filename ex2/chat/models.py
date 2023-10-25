from django.db import models


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
