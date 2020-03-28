# from django.db import models
from pymongo import MongoClient
from decouple import config
from nltk import corpus

# Create your models here.

client = MongoClient(config("DATABASE_HOST"), config("DATABASE_PORT", cast=int))
db = client.dbbot


def exist_words(word: str) -> True or False:
    """
    Verifica se uma palavra já existe na collection stopwords.
    :param word: Uma palavra a ser verificada
    :type word: str
    :return:True or False
    :rtype: bool
    """
    stopwords = db.stopwords
    #word_obj = stopwords.aggregate([{"$unwind": "$words"}, {"$match": {"words": word}}])
    word_obj = stopwords.find_one({"words": word})
    if word_obj is None:
        return False
    return True


def message():
    """
    Faz um find na collection message buscando todas as palavras dentro da collection.
    :return: Retorna a lista contendo todas as mensagens encontradas exceto mensagens já ignoradas.
    :rtype: list
    """
    messages = []
    msg = db.message.find()
    for m in msg:
        message_obj = m.get('msg')
        if message_obj is not None and message_obj.__contains__('/9j/'):
            continue
        messages.append(message_obj)
    return messages

### Preciso trabalhar Stopwords function ###
def stopwords():
    stop_words = corpus.stopwords.words('portuguese')
    new_words = append_words(stop_words)
    # Preciso tratar generator abaixo.
    new_words.append(lambda x: x for x in corpus.stopwords.words('english'))
    #print(new_words)
    return new_words


def save_words(element_words: list) -> True or False:
    """
    Salva as palavras na collection de stopwords.
    :param element_words: Palavra a ser salva.
    :type element_words: str
    :return: True or False
    :rtype: bool
    """
    stopwords = db.stopwords
    cont = 0
    for word in element_words:
        word_obj = word.upper()
        if exist_words(word_obj) is False:
            stopwords.update_one({'_id': 1}, {'$push': {'words': word_obj}})
            cont += 1
        continue
    if cont == 0:
        return ['False', cont]
    return ['True', cont]
