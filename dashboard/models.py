# from django.db import models
from pymongo import MongoClient
from decouple import config
from nltk import corpus
from wordcloud import STOPWORDS


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
    word_obj = stopwords.find_one({"words": word})
    if word_obj is None:
        return False
    return True


def message(chat):
    """
    Faz um find na collection message buscando todas as palavras dentro da collection.
    :return: Retorna a lista contendo todas as mensagens encontradas exceto mensagens já ignoradas.
    :rtype: List
    """
    messages = []
    if chat == 'None':
        message_obj = db.message.find()
        for item in message_obj:
            message = item.get('msg')
            if message is None:
                continue
            else:
                messages.append(message)
        return messages
    message_obj = db.message.find({'chat_name': chat})
    for item in message_obj:
        message = item.get('msg')
        if message is None:
            continue
        else:
            messages.append(message)
    return messages


def stopwords():
    """
    Função que faz a verificação da existência de uma palavra em banco de dados e em sua ausência faz o salvamento.
    :return: Retorna lista de stopwords.
    :rtype: List
    """
    stopwords = db.stopwords
    stop_words = list(STOPWORDS)
    for elem in stop_words:
        word = elem.upper()
        if exist_words(word) is False:
            stopwords.update_one({'_id': 1}, {'$push': {'words': word}})
    stops_obj = db.stopwords.find({})
    for elem in stops_obj:
        stops = elem.get('words')
    return stops


def save_words(element_words: list) -> list:
    """
    Salva as palavras na collection de stopwords.
    :param element_words: Palavra a ser salva.
    :type element_words: str
    :return: str(True or False) + cont
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


def get_chats():
    """
    Função que faz a busca por chats na base de dados.
    :return: Lista de chats
    :rtype: list.
    """
    chats = db.chat
    chats_obj = chats.find({}, {'chat': 1, '_id': 0})
    chat = []
    for item in chats_obj:
        chat.append(item.get('chat'))
    return chat
