from django.db import models

from users.models import User
from chat.models import Chat


STATUS_CHOICES = (
    ("opened" , "opened"),
    ("closed", "closed"),
    ("waiting for response", "waiting for response"),
    ("waiting for treatment", "waiting for treatment"),
)


class Form(models.Model):
    open_date = models.DateField()
    close_date = models.DateField()
    event_reporter = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    event_status = models.CharField(max_length=100,
                                    choices=STATUS_CHOICES,
                                    default="OPEN")
    ability_open_a_draft = models.BooleanField(default=False)
    ability_download_form_archive = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(User, related_name="shared_users", blank=True)


class FileSharingForm(Form):
    file_upload_date = models.DateField()
    upload_file_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    file = models.FileField()


class MessagesForm(Form):
    chat_id = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    

