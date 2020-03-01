from django.shortcuts import render, redirect
from django.contrib import messages
from .models import message, stopwords, save_words
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dashboard.classes.normalizer import Normalize
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
        if file.name[-4:] in ['.csv', '.txt']:
            normalized = Normalize(file)
            set_list = normalized.normalize_sep()
            for element_list in set_list:
                if save_words(element_list) is True:
                    messages.success(request, 'Novas palavras cadastradas com sucesso!') # => preciso adicionar as mensagens padrão.
                    return redirect(request, wordcloud)
    # Faça algo
       