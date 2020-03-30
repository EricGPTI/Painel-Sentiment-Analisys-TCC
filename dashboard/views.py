from django.shortcuts import render, redirect
from django.contrib import messages
from .models import message, stopwords, save_words
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dashboard.classes.normalizer import Normalize
import os

# Create your views here.


def home(request):
    return render(request, 'index.html')


def wordcloud(request):
    stop = func_stopwords()
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
    stops = stopwords()
    w_cloud = WordCloud(stopwords=stops, background_color="black").generate(all_summary)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(w_cloud, interpolation='bilinear')
    plt.tight_layout()
    plt.show()
    return wordcloud(request)


def process_stops(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        if file.name[-4:] in ['.csv', '.txt']:
            normalized = Normalize(file)
            set_list = normalized.normalize_sep()
            cont = 0
            for element_list in set_list:
                words_saved = save_words(element_list)
                cont += words_saved[1]
            if words_saved[0] is 'True':
                messages.success(request, f'{cont} novas palavras cadastradas com sucesso!')
                return redirect(stop)
            messages.warning(request, 'Nenhuma nova palavra foi adicionada.')
            return redirect(stop)
        messages.warning(request, 'Seu arquivo não é um arquivo texto ou csv.')
        return redirect(stop)
