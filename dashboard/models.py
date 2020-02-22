#from django.db import models
from djongo import models

# Create your models here.


class Message(models.Model):
    _id = models.ObjectIdField()
    msg_id = models.CharField(max_length=255)
    msg_type = models.CharField(max_length=255)
    msg_chat_id = models.CharField(max_length=255)
    msg_sender_id = models.CharField(max_length=255)
    msg_sender = models.CharField(max_length=255)
    msg_date = models.DateTimeField()
    msg = models.TextField()

    class Meta:
        ordering = ['msg_date']