import sys
from formatter.simple_format import Formatter
from helper.from_file import format_from_file
from django.template.defaultfilters import lower


def main(lenght=40, justify=False):
    #Lê todo o arquivo e processa (cuidado com o tamanho do arquivo)
    #Processa uma string
    formater = Formatter(lenght, justify)
    text = formater.text_format("In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day.")
    print(text)

    #Processa a partir de um arquivo
    text = format_from_file("helper/text.txt", lenght, justify)
    print(text)

if __name__ == "__main__":
    lenght = 40
    if len(sys.argv) > 1:
        try:
            lenght=int(sys.argv[1])
        except:
            lenght = 40

    justify = False
    if len(sys.argv) > 2:
        justify=True if lower(sys.argv[2]) == 'true' else False
    
    main(lenght, justify)