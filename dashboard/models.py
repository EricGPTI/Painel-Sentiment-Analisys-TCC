# from django.db import models
from pymongo import MongoClient
from decouple import config

# Create your models here.

client = MongoClient(config("DATABASE_HOST"), config("DATABASE_PORT", cast=int))
db = client.dbbot


def message():
    messages = []
    msg = db.message.find()
    for m in msg:
        messages.append(m['msg'])
    return messages


#class Message(models.Model):
#    _id = models.ObjectIdField()
#    msg_id = models.CharField(max_length=255)
#    msg_type = models.CharField(max_length=255)
#    msg_chat_id = models.CharField(max_length=255)
#    msg_sender_id = models.CharField(max_length=255)
#    msg_sender = models.CharField(max_length=255)
#    msg_date = models.DateTimeField()
#    msg = models.TextField()
#
#    class Meta:
#        ordering = ['msg_date']