# Desafio 1: Strings

Após ler o coding style do kernel Linux, você descobre a mágica que é
ter linhas de código com no máximo 80 caracteres cada uma.

Assim, você decide que de hoje em diante seus e-mails enviados também
seguirão um padrão parecido e resolve desenvolver um plugin para te ajudar
com isso. Contudo, seu plugin aceitará no máximo 40 caracteres por linha.

Implemente uma função que receba:
1. um texto qualquer
2. um limite de comprimento

e seja capaz de gerar os outputs dos desafios abaixo.

## Exemplo input

`In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.`

`And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.`

O texto deve ser parametrizável e se quiser, pode utilizar um texto de input de sua preferência.

### Parte 1 (Básico) - limite 40 caracteres
Você deve seguir o exemplo de output [deste arquivo](https://github.com/idwall/desafios/blob/master/strings/output_parte1.txt), onde basta o texto possuir, no máximo, 40 caracteres por linha. As palavras não podem ser quebradas no meio.

### Parte 2 (Intermediário) - limite 40 caracteres
O exemplo de output está [neste arquivo](https://github.com/idwall/desafios/blob/master/strings/output-parte2.txt), onde além de o arquivo possuir, no máximo, 40 caracteres por linha, o texto deve estar **justificado**.

### Dicas
- Existe um template para projetos em Java ;)

### Extras

- Parametrização da quantidade de caracteres por linha.

### Pacotes adicionais

- Nenhum

### Como utilizar

Importe a classe Formatter:
```python
from formatter.simple_format import Formatter
```
	
Ela tem dois parâmetros:
1. lenght: comprimento da linha (se omitida adotará 40 por padrão)
2. justify: Se verdadeiro `True` irá justivicdar o texto, caso `False` não (por padrão é `False`)

### Como usar
Nesta caso, como não há parâmetros, irá assumir tamanho da linha = 40 e não irá justificar:
```python
formater = Formatter()
text = formater.text_format("In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day.")
print(text)
```
 Saída:
```
In  the  beginning  God  created  the  heavens  and the earth. Now the earth was
formless and empty, darkness was over the surface of the deep, and the Spirit of
God was hovering over the waters.

And  God said, "Let there be light," and there was light. God saw that the light
was  good,  and  he  separated the light from the darkness. God called the light
"day,"  and the darkness he called "night." And there was evening, and there was
morning - the first day.
```
 
Para Justificar:
```python
formater = Formatter(justify=True)
text = formater.text_format("In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n\nAnd God said, \"Let there be light,\" and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light \"day,\" and the darkness he called \"night.\" And there was evening, and there was morning - the first day.")
print(text)
```

Saída:
```
In the beginning God created the heavens
and   the   earth.  Now  the  earth  was
formless  and  empty,  darkness was over
the  surface of the deep, and the Spirit
of God was hovering over the waters.

And  God said, "Let there be light," and
there  was light. God saw that the light
was  good,  and  he  separated the light
from  the darkness. God called the light
"day,"   and   the  darkness  he  called
"night."  And  there  was  evening,  and
there was morning - the first day.
 ```

### Teste rápido
Basta executar o script abaixo. Ele aceita os mesmo dois parâmetros que a classe via linha de comando (`lenght` e `justify`).
```python
python test_formatter.py
```
ou 
```python
python test_formatter.py 10 True
```

Saída (um texto fomatado por string e outro por arquivo em `helper/text.txt`):
```
In the beginning God created the heavens
and the earth. Now the earth was
formless and empty, darkness was over
the surface of the deep, and the Spirit
of God was hovering over the waters.

And God said, "Let there be light," and
there was light. God saw that the light
was good, and he separated the light
from the darkness. God called the light
"day," and the darkness he called
"night." And there was evening, and
there was morning - the first day.

In the beginning God created the heavens
and the earth. Now the earth was
formless and empty, darkness was over
the surface of the deep, and the Spirit
of God was hovering over the waters.

And God said, "Let there be light," and
there was light. God saw that the light
was good, and he separated the light
from the darkness. God called the light
"day," and the darkness he called
"night." And there was evening, and
there was morning - the first day.
```

### Considerações
Este foi o primeiro que fiz e foi divertido.

Ao analisar o código tenha em mente:

* Fiz estes código à noite, após um dia de trabalho
* Tive apenas 3 noites para fazer este desafio e o crawlers
* Fiz o melhor possível, até fiz um importador de texto, tudo muito simples, dada a falta de tempo (foi informado que tinha 5 dias a contar de segunda)

Obrigado pelo desafio :-) 
