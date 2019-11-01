import io

def format_from_file(file_name='text.txt',lenght=40, justify=False):
    """ Lê um arquivo de texto, linha por lina e deixa cada uma com no máximo 'lenght' caracteres.
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
    # Abre o arquivo
    file = open(file_name, "r");
    
    formated_text = ''
    # Lê linha por linha
    for line in file.readlines():
        # Formata cada linha com a nova largura
        formated_text += line_format(line, lenght, justify)
        
    file.close()
    
    return formated_text

def text_from_file(file_name='text.txt'):
    """ Lê todo o texto de um arquivo

    :param file_name: Caminho completo, incluindo o nome para o arquivo
    :type file_name: string

    :return: Todo o texto do arquivo (cuidado com o tamanho, não tem tratamento)
    :rtype: string
    
    """
    #Abre o arquivo e lê todo o conteúndo e retorna
    file = open(file_name, "r");
    text = file.read()
    file.close()
    
    return text

def text_format(text, lenght=40, justify=False):
    """ Lê um arquivo de texto, linha por lina e deixa cada uma com no máximo 'lenght' caracteres.
    Também pode justificar o texto.
    
    :param text: Texto que terá suas linhas reformatadas
    :type text: string
    
    :param lenght: Total de caracteres por linha
    :type lenght: int

    :param justify: Se True justifica o texto
    :type justify: boolean

    :return: Texto com a nova largura de linhas
    :rtype: string
    """
    
    #Cria um bufferIO para poder linha a linha
    text_buffer = io.StringIO(text)
    justified_text = ''
    for line in text_buffer:
        # Lê todas as linhas do texto e formata para o novo tamanho
        justified_text += line_format(line, lenght, justify)
            
    return justified_text

def line_format(line_text, lenght=40, justify=False):
    """ Keep the lines with 'lenght' characters
    
    :param line_text: Uma linha normal que será formata para um novo tamanho
    :type line_text: string

    :param lenght: Total de caracteres por linha 
    :type lenght: int

    :param justify: Se True justifica o texto
    :type justify: boolean
    
    :return: Texto com a nova largura de linhas
    :rtype: string
    """
    
    # se a linha for vazio retorna uma quebra de linha
    if(line_text == '' or line_text == "\n"):
        return "\n"
    
    line = ''
    text_in_lines = ''
    
    #Palavras separadas por espaço
    text_splitted = line_text.split()
    #Quantidade de palavras
    blocks = len(text_splitted)
    
    #Itera todos os blocos de palavras
    for index, word in enumerate(text_splitted):
        if index == 0:
            #Primeiro bloco, apenas adiciona ao retorno
            line = word
        else:
            if( len(line)+len(" "+word) <= lenght):
                #Se não atingiu o máximo possível (lenght), concatena um espaço e a palavra
                line += " " + word
            else:
                #Aqui a linha está completa
                if justify == True:
                    #como a linha está completa, verifica se precisa ou não justivicar
                    line = line_justify(line, lenght)
                
                #Adiciona a linha e uma quebra de linha 
                text_in_lines += line
                text_in_lines += "\n"
                #O próximo bloco já é a próxima linha
                line = word

            # Se chegou ao fim (então soma última linha)
            if(index == blocks -1):
                text_in_lines += line
                text_in_lines += "\n"
    
    return text_in_lines

def line_justify(text_line, lenght=40):
    """ Justifica o texto em 'lenght' caracteres

    :param text_line: Linha que seja justivida
    :type text_line: string
    
    :param lenght: Total de caracteres por linha 
    :type lenght: int

    :return: justified text
    :rtype: string
    """
    # Comprimento do texto
    text_lenght = len(text_line)
    
    #Não tem como justificar uma linah que maior que o tamanho lenght
    if text_lenght >= lenght:
        return text_line
    
    #Separa em blocos de palavras
    text_splitted = text_line.split()
    word_count = len(text_splitted)
    #A quantidade de espaços é total de blocos menos 1
    between_worlds_for_spaces = word_count - 1
    new_text = ''
    
    #Precisa existir ao menos duas palavras
    if word_count > 1:
        """
        A diferença entre o comprimento da linha desejada e o tamanho da linha
        indica a quantidade de espaços a serem adicionados
        """
        aditional_spaces = lenght - text_lenght
        """
        Espaços totais é o total de palavras -1 mais os espaços adicionais
        Ou seja, é a quantidade de espaços existentes mais a direfença em relação
        ao comprimento da linha e o tamanho a ser justificado
        """
        total_spaces = (word_count-1)+aditional_spaces

        #Quantos espaços serão adicionados entre as palavras (a difereça será calculada mais abaixo)
        spaces_between_words = ( total_spaces // between_worlds_for_spaces )
        #Criar uma lista com os elementos iguais, que é o tanto de espaços entre cada palavrasa
        list_spaces = [spaces_between_words] * between_worlds_for_spaces
        """
        O resto entre o total de espaços a serem adicionadoa e a quantidade de palavras -1
        indica quantos espaços a mais tenho que adicionar, eles são adicionados ao início
        da lista 
        """
        for index in range(0,  total_spaces % between_worlds_for_spaces):
            list_spaces[index] += 1
        
        # Agora é só correr a lista de palavras e adicionar os espaços
        for index, word in enumerate(text_splitted):
            if index == 0:
                #Primeiro iteração vai são a palavra
                new_text += word
            else:
                #Adiciona a quantidade de espaços entre as palavras
                new_text +=  " " * list_spaces[index-1]
                new_text += word
    
    else:
        # Só tem uma palavra, então retorna ela
        new_text = text_line

    return new_text
        

def main():
    #Lê todo o arquivo e processa (cuidado com o tamanho do arquivo)
    text = text_from_file()
    print(text_format(text, 40, True))
    #Processa uma string
    print(text_format("In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day.", 40, True))
    #Processa linha por lina, evitando problemas de arquivos grandes
    print(format_from_file("text.txt", 40, True))
    
if __name__ == "__main__":
    main()
