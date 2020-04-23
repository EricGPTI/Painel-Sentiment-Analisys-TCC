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


logging.basicConfig(filename='log.txt', level=logging.WARNING)


def home(request):
    """
    Função de View usada para chamar a url principal.
    :return: Retorna um template html renderizado no navegador.
    """
    return render(request, 'index.html')


def wordcloud(request):
    """
    Função de View para acesso à página de wordcloud.
    :return: Retorna um template html juntamente com um um dicionário de dados contendo todos os chats.
    """
    chat = get_chats()
    return render(request, 'wordcloud.html', {'chats': chat[0]})


def stop(request):
    """
    Função de View para acesso à página de cadastro de stopwords.
    :return: Retorna um template html para a mesma página.
    """
    return render(request, 'stop.html')


def func_stopwords():
    """
    Função que chama o model stopwords na busca por palavras deste grupo.
    :return: Retorna a lista de stopwords.
    :rtype: List
    """
    stops = stopwords()
    return stops


def validate_img(file):
    """
    Função que valida a existência de arquivo de imagem de wordcloud para exibição no template.
    :param file: Variável que recebe o caminho do arquivo.
    :type file: Variável do tipo string.
    :return: Return True ou False.
    :rtype: Bool.
    """
    if os.path.isfile(file):
        if os.path.isfile(file):
            return True
        return False
    return False


def update(request):
    """
    Função para criar uma nuvem de palavras.
    :return: Retorna uma chamada de função de view wordcloud.
    """
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

            w_cloud_file = os.path.join(config('PATH_IMG'), 'wordcloud.jpg')
            w_cloud1_file = os.path.join(config('PATH_IMG'), 'wordcloud1.jpg')

            if validate_img(w_cloud_file) is False:
                plt.savefig(w_cloud_file, dpi=300, quality=100, format='jpg')
                return wordcloud(request)
            elif validate_img(w_cloud1_file) is False:
                plt.savefig(w_cloud1_file, dpi=300, quality=100, format='jpg')
                os.remove(w_cloud_file)
                return wordcloud(request)
            os.remove(w_cloud_file)
            os.remove(w_cloud1_file)
            plt.savefig(w_cloud_file, dpi=300, quality=100, format='jpg')
            return wordcloud(request)

            #    w_cloud1_file = os.path.join(config('PATH_IMG'), 'wordcloud1.jpg')
            #    if not os.path.isfile(config('PATH_IMG'), 'w_cloud1_file'):
            #        #plt.savefig(os.path.join(config('PATH_IMG'), 'wordcloud1.jpg'), dpi=300, quality=100, format='jpg')
            #        return wordcloud(request)
            #    else:
            #
            #        #
            #        #os.remove(w_cloud1_file)
        except ValueError:
            messages.info(request, 'Não existe quantidade mínima de palavras para este chat.')
            return wordcloud(request)


def process_stops(request):
    """
    Função que faz o processamento de arquivos do tipo .txt ou .csv inserção de novas palavras na collection
    de stopwords.
    :return: Faz um redirect para a página stop.
    """
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
