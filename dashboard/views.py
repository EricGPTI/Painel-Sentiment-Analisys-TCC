from django.shortcuts import render, HttpResponse
from .models import message, stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dashboard.classes.delimiter import Delimiter
import os

# Create your views here.


def home(request):
    return render(request, 'index.html')


def wordcloud(request):
    return render(request, 'wordcloud.html')


def dashboard(messages):
    pass


def stop(request):
    return render(request, 'stop.html')


def func_stopwords():
    stops = stopwords()
    return stops


def update(request):
    messages = message()
    summary = []
    for m in messages:
        if m is not None:
            summary.append(m)
    all_summary = ",".join(s for s in summary)
    stops = func_stopwords()
    wordcloud = WordCloud(stopwords=stops, background_color="black").generate(all_summary)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    plt.tight_layout()
    plt.show()
    return wordcloud(request)


def process_stops(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        delimiter = request.POST['delimiter']
        print(type(file))
        if file.name[-4:] in ['.csv', '.txt']:
            list_file = file.read().decode('utf-8').splitlines()
            for line in list_file:
                adjust = Delimiter(line)
                new_line = adjust.test()
                print(new_line)
        return HttpResponse(file.name)
    # Faça algo
        
