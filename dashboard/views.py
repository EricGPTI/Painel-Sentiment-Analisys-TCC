from django.shortcuts import HttpResponse, render
from .models import message
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from pymongo import MongoClient
#from decouple import config


#client = MongoClient(config('DATABASE_HOST'), config('DATABASE_PORT', cast=int))
#db = client.dbbot

# Create your views here.


def home(request):
    return render(request, 'index.html')


def wordcloud(request):
   return render(request, 'wordcloud.html')


def dashboard(messages):
    for msg in messages:
        print(msg)


def stopwords(messages):
    stopwords = set(STOPWORDS)
    return stopwords


def update(request):
    messages = Message.objects.filter()
    dashboard(messages)
    return wordcloud(request)
    
    #all_summary = " ".join(s for s in messages)

    #stop = stopwords(messages)
    #wordcloud = WordCloud(stopwords=stop, background_color="black").generate(all_summary)

