# from django.db import models
from pymongo import MongoClient
from decouple import config
from nltk import corpus

# Create your models here.

client = MongoClient(config("DATABASE_HOST"), config("DATABASE_PORT", cast=int))
db = client.dbbot


def message():
    messages = []
    msg = db.message.find()
    for m in msg:
        message_obj = m.get('msg')
        if message_obj is not None and message_obj.__contains__('/9j/'):
            continue
        messages.append(message_obj)
    return messages


def stopwords():
    stop_words = corpus.stopwords.words('portuguese')
    stop_words.append(x for x in ['9j', '4AAQSKZJRgABAAQAAAQABAAD', 'MediaMessage', 'MMSMessage'])
    stop_words.append(corpus.stopwords.words('english'))
    return stop_words
