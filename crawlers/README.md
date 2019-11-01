# Desafio 2: Crawlers

Parte do trabalho na IDwall inclui desenvolver *crawlers/scrapers* para coletar dados de websites.
Como nós nos divertimos trabalhando, às vezes trabalhamos para nos divertir!

O Reddit é quase como um fórum com milhares de categorias diferentes. Com a sua conta, você pode navegar por assuntos técnicos, ver fotos de gatinhos, discutir questões de filosofia, aprender alguns life hacks e ficar por dentro das notícias do mundo todo!

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com threads contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o "/r/AskReddit".

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

Sua missão é encontrar e listar as *threads* que estão bombando no Reddit naquele momento!
Consideramos como bombando *threads* com 5000 pontos ou mais.

## Entrada
- Lista com nomes de subreddits separados por ponto-e-vírgula (`;`). Ex: "askreddit;worldnews;cats"

### Parte 1
Gerar e imprimir uma lista contendo a pontuação, subreddit, título da thread, link para os comentários da thread e link da thread.
Essa parte pode ser um CLI simples, desde que a formatação da impressão fique legível.

### Parte 2
Construir um robô que nos envie essa lista via Telegram sempre que receber o comando `/NadaPraFazer [+ Lista de subrredits]` (ex.: `/NadaPraFazer programming;dogs;brazil`)

### Dicas
 - Use https://old.reddit.com/
 - Qualquer método para coletar os dados é válido. Caso não saiba por onde começar, procure por JSoup (Java), SeleniumHQ (Java), PhantomJS (Javascript) e Beautiful Soup (Python).

### Pacotes adicionais
Depende de [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).
Instale via `pip` ou siga as instruções na página acima (eu usei o `pip`):
```
pip install pyTelegramBotAPI
```

### Como utilizar
Existe a classe `Reddit` que é um *scraper*, que pode ser utilizada independente da parte do código que interage com o *Telegram*.
Para usar basta importar o pacote e instânciar a classe:
```python
from scraper.reddit import Reddit
reddit_scraper = Reddit()
```
Utile o método `sub_reddits_for_telegram` que rebece um texto com subreddits separados por ponto-e-vírgula (`;`). Os dados serão retirados do site [Old Reddit](https://old.reddit.com/). O resultado é uma lista, onde cada elemento é um `dict` com esta estrutura:

`
[{'post': post_tile, 'markup': markup, 'line': post_title_line}', ...]
`
Onde:
1. 'post': Quantidade de likes + o subreddit
2. 'markup': É um markup para exibir botões no lugar da linha flat
3. 'post_title_line': é um texto já preparado para o Telegram: `35.5k/news: Trump, Lifelong New Yorker, Declares Him... Comments`.

Para um rápido teste basta executar:
```
python reddit.py
```
Será exibida todos os subreddits das categorias `askreddit`, `worldnews` e `cats` com até 500 likes.

A parte do *Telegram* é um bot que responde a 2 comandos: `/NadaPraFazer` e `/NadaPraFazerB`, onde:
- NadaPraFazer: retorna a lista de subreddits enviados como parâmetros e com mais de 5000 likes no formato de linhas com links
- NadaPraFazerB: Faz a mesma coisa, mas exibe dois botões no lugar de links: Post e Comentários

Antes de executar o Telegram Bot será necessário colocar o `TOKEN` no arquivo `config.py`:

```python
TOKEN = 'xxxxxxxxx:sssssssssssssssssssssssssssssssssss'
```

Para executar o bot, basta executar este comando:
```
python telegram_bot.py
```
### No Telegram
![Telegram](https://raw.githubusercontent.com/edermartins/desafios/master/reddit_telegram.JPG)

### Considerações
Eu nunca havia usado o telegram e decidi utilizar o `pyTelegramBotAPI` indicado na página do próprio Telegram: [core.telegram.org](https://core.telegram.org/bots/samples) na parte de `Python`.

Ao analisar este pacote tenha em mente:
* Assim como aconteceu com desafio/strings, eu tive apenas 3 noites, pois eu tinha 2 compromissos nesta semana
* Foi bem legal trabalhar com o Telegram. Fiz uma versão com mensagens em modo texto e outra com botões

Obrigado por este desafio

