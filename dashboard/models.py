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
    new_words = append_words(stop_words)
    # Preciso tratar generator abaixo.
    new_words.append(lambda x: x for x in corpus.stopwords.words('english'))
    print(new_words)
    return new_words


def append_words(stop_words):
    stop_w = stop_words
    words = ['9j', '4AAQSKZJRgABAAQAAAQABAAD', 'MediaMessage', 'MMSMessage', 'note', 'https']
    for w in words:
        stop_w.append(w)
    return stop_w
