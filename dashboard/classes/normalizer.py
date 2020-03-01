class Normalize:
    """
    Classe de tratamento de arquivos de acordo com o delimitador e quebra de linhas.
    """
    def __init__(self, file):
        self.file = file

    def normalize_sep(self):
        """
        Faz o split a partir do caracter Pipe |
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        bag_of_words = []
        list_file = self.file.read().decode('utf-8').splitlines()
        for line in list_file:
            line_obj = line.replace('"', '').replace(' ', '').replace('|', ',').replace(';', ',').split(',')
            bag_of_words.append(line_obj)
        return bag_of_words

