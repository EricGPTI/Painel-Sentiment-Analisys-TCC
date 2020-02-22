from django.shortcuts import render, HttpResponse
from dashboard.models import Message
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Create your views here.


def wordcloud(request):
    messages = Message.objects.all()
    for msg in messages:
        print(msg)
    return HttpResponse(str(messages))
    


def stopwords():
    pass


