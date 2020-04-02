from django.shortcuts import render, redirect
from django.contrib import messages
from .models import message, stopwords, save_words, get_chats
import matplotlib
matplotlib.use('Agg')
from decouple import config
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dashboard.classes.normalizer import Normalize
import os
import logging

# Create your views here.

logging.basicConfig(filename='log.txt', level=logging.WARNING)

def home(request):
    return render(request, 'index.html')


def wordcloud(request):
    chat = get_chats()
    return render(request, 'wordcloud.html', {'chats': chat[0]})


def dashboard(messages):
    pass


def stop(request):
    return render(request, 'stop.html')


def func_stopwords():
    stops = stopwords()
    return stops


def update(request):
    stop = func_stopwords()
    if request.method == 'POST':
        chat = request.POST.get('chat')
        msgs = message(chat)
        summary = []
        for m in msgs:
            if m is not None:
                m = m.upper()
                summary.append(m)
        all_summary = ",".join(s for s in summary)
        stops = stopwords()
        try:
            w_cloud = WordCloud(stopwords=stops, background_color="black").generate(all_summary)
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(w_cloud, interpolation='bilinear')
            ax.set_axis_off()
            plt.tight_layout()
            if os.path.exists(config('PATH_IMG')) is True:
                os.remove(config('PATH_IMG'))
                plt.savefig(config('PATH_IMG'), dpi=300, quality=100, format='jpg')
                return wordcloud(request)
            else:
                plt.savefig(config('PATH_IMG'), dpi=300, quality=100, format='jpg')
                return wordcloud(request)
        except ValueError:
            messages.info(request, 'Não existe quantidade mínima de palavras para este chat.')
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
