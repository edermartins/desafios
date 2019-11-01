from formatter.simple_format import Formatter

def format_from_file(file_name=None,lenght=40, justify=False):
    """
    Lê um arquivo de texto, linha por lina e deixa cada uma com no máximo 'lenght' caracteres.
    Também pode justificar o texto.
    
    :param file_name: Caminho completo, incluindo o nome para o arquivo
    :type file_name: string
    
    :param lenght: Largura para as novas linhas
    :type lenght: int

    :param justify: Se True justifica o texto
    :type justify: boolean

    :return: Texto com a nova largura de linhas
    :rtype: string
    """
    formated_text = ''
    if file_name:
        try:
            # Abre o arquivo
            file = open(file_name, "r");
            
            formated_text = ''
            # Lê linha por linha
            for line in file.readlines():
                # Formata cada linha com a nova largura
                formated_text += Formatter.line_format(line, lenght, justify)
            
            file.close()
            
        except IOError:
            print("ERRO ao tentar abrir o arquivo '{}'".format(file_name))
    
    return formated_text

def text_from_file(file_name=None):
    """
    Lê todo o texto de um arquivo

    :param file_name: Caminho completo, incluindo o nome para o arquivo
    :type file_name: string

    :return: Todo o texto do arquivo (cuidado com o tamanho, não tem tratamento)
    :rtype: string
    
    """
    
    text = ''
    if file_name:
        try:
            #Abre o arquivo e lê todo o conteúndo e retorna
            file = open(file_name, "r");
            text = file.read()
            file.close()

        except IOError:
            print("ERRO ao tentar abrir o arquivo '{}'".format(file_name))
    
    return text