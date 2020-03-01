class Delimiter:
    """
    Classe de tratamento de arquivos de acordo com o delimitador e quebra de linhas.
    """
    def __init__(self, line):
        self.line = line

    def pipe(self):
        """
        Faz o split a partir do caracter Pipe |
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        new_line = self.line.replace('"', '')
        new_line = new_line.replace(' ', '')
        new_line = new_line.replace('|', ',')
        new_line = new_line.replace(';', ',')
        return new_line

    def comma(self):
        """
        Faz o split a partir do caracter Vírgula ,
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        new_line = self.line.replace('"', '')
        new_line = new_line.replace(' ', '')
        new_line = new_line.replace('|', ',')
        new_line = new_line.replace(';', ',')
        return new_line

    def semicolon(self):
        """
        Faz o split a partir do caracter ponto e vírgula ;
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        new_line = self.line.replace('"', '')
        new_line = new_line.replace(' ', '')
        new_line = new_line.replace('|', ',')
        new_line = new_line.replace(';', ',')
        return new_line

    

    def semicolon(self):
        """
        Faz o split a partir do caracter ponto e vírgula ;
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        new_line = self.line.replace('"', '')
        new_line = new_line.replace(' ', '')
        new_line = new_line.replace('|', ',')
        new_line = new_line.replace(';', ',')
        return new_line

    

    def semicolon(self):
        """
        Faz o split a partir do caracter ponto e vírgula ;
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        new_line = self.line.replace('"', '')
        new_line = new_line.replace(' ', '')
        new_line = new_line.replace('|', ',')
        new_line = new_line.replace(';', ',')
        return new_line

    
    def test(self):
        """
        Faz o split a partir do caracter ponto e vírgula ;
        :param line: linha a ser tratada.
        :return: retorna uma lista com dados tratados.
        """
        new_line = self.line.replace('"', '')
        new_line = new_line.replace(' ', '')
        new_line = new_line.replace('|', ',')
        new_line = new_line.replace(';', ',')
        return new_line
