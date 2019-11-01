import json
import requests
from bs4 import BeautifulSoup
import re 

class Reddit:
    
    def __init__(self, url_base=None):
        """
        Construtor precisa receber o endereço do Reddit

        :param url_base: URL base para a busca no Reddit
        :type url_base: string
        """
        # Url base precisa ter um mínimo de 10 caracteres
        if url_base in ('', None) or len(url_base) <= 10:
            # Se não vier URL, então assime essa
            self.url_base = 'https://old.reddit.com'
        else:
            #Por hora está sem tratamento para verificar se realmente é uma URL
            self.url_base = url_base[0:-1] if url_base[-1] == '/' else url_base
        

    def _parse_likes_to_float(self, likes):
        """
        Converte valores com representação textual, tais como 6.2k para 6200

        :param likes: Quantidade de like formatada nn.nk ou nn.nm
        :type likes: string

        :return: Retorna o valor convertido para um inteiro
        :rtype: int
        """
        
        # Deixa somente caracteres númericos e pontos
        float_list = re.findall(r"\d*\.\d+|\d+", likes)
        #Verifica se sovou alguma coisa, senão devolve 0
        if len(likes) > 0 and len(float_list) > 0:
            #Converte para float para poder, eventualmente, fazer a multiplicação
            float_view = float(float_list[0])
            multiplier = 1000
            #Lê o último caracter para idenfificar o multiplicador
            last_character = likes[-1].lower()
            if last_character == 'k': # k = kilo = 1000
                result = int(float_view * multiplier)
            elif last_character == 'm':# m = mega = 1000000
                result = int(float_view * multiplier**2)
            else:# unitário, apenas converte em inteiro e retorna
                result = int(float_view)
        else:
            result = 0
        
        return result
    
    def _telegram_str(self, posts, line_size=40):
        """
        Converte a lista em texto formatado para o telegram
        
        :param posts: Lista de posts neste formato: [{"rank": x, "likes": y,
        "title": 'Aa', "comments_href": '#', "title_href": '#'},...]
        :type posts: list
        
        :return: Lista com o texto formatado para o Telegram. Formato:
        [{'post': post_tile, 'markup': markup}', ...]
        :rtype: list
        """
        result = []
        for post in posts:
            title = post['title'][0:line_size]+'...' if len(post['title']) > line_size else post['title']
            post_tile_buttons = "{0}/{1}: {2}".format(post['likes'], post['subreddit'], title)
            markup = {"inline_keyboard": 
                [[
                    {"text": 'Post',"url": post['title_href']},
                    {"text": "Commentários","url": post['comments_href']}
                ]]
            }
            post_title_line = "{0}/{1}: [{2}]({3}) [Comments]({4})".format(post['likes'], post['subreddit'], title, post['title_href'], post['comments_href'])
            markup = json.dumps(markup) 
            result.append({'post': post_tile_buttons, 'markup': markup, 'line': post_title_line})
            
        return result
    
    def sub_reddits_for_telegram(self, subreddits, points=5000, separator=';'):
        """
        Busca dados (scrape) um sub reddit com certa quantidade de likes
        e retorna uma lista formatada para o Telegram
        
        :param subreddit: Sub reddit. Exemplo: cat
        :type subreddit: string
        
        :param points: Quantidade mínima de likes para entrar na lista
        :type points: int
    
        :param separator: Texto usado para separa as palavras, por padrão ';'
        :type separator: string
    
        :return: Lista com o texto formatado para o Telegram. Formato:
        """
        return self._telegram_str(self.sub_reddits(subreddits, points=points, separator=separator))
        
      
    def sub_reddits(self, subreddits, points=5000, separator=';'):
        """
        Busca dados (scrape) um sub reddit com certa quantidade de likes
        
        :param subreddit: Sub reddit. Exemplo: cat
        :type subreddit: string
        
        :param points: Quantidade mínima de likes para entrar na lista
        :type points: int
    
        :param separator: Texto usado para separa as palavras, por padrão ';'
        :type separator: string
    
        :return: Um list de dict com o resultado. Exemplo: [{"rank": x, "likes": y,
        "title": 'Aa', "comments_href": '#', "title_href": '#'},...]. Ou [] se houve algum erro
        :rtype: list
        """
        reddits = []
        #Separa o texto separado por separator em lista
        subreddits_list = subreddits.split(separator)
        
        #Faz uma chamada para cada elemento da lista
        for subreddit in subreddits_list:
            reddits += self.sub_reddit(subreddit=subreddit, points=points)
        
        return reddits
        
    def sub_reddit(self, subreddit, points=5000, headers=None):
        """
        Busca dados (scrape) um sub reddit com certa quantidade de likes
        
        :param subreddit: Sub reddit. Exemplo: cat
        :type subreddit: string
        
        :param points: Quantidade mínima de likes para entrar na lista
        :type points: int
    
        :param headers: Caso não esteja presente o site old.reddit.com rejeita seguidas tentativas
        :type headers: dict
    
        :return: Um list de dict com o resultado. Exemplo: [{"rank": x, "likes": y, "title": 'Aa',
        "comments_href": '#', "title_href": '#'},...]. Ou [] se houve algum erro
        :rtype: list
        """
        if headers is None:
            # Tive que adicionar este cabeçalho, pois o old.reddit.com parou de me aceitar
            # sem ele, devolvendo sempre HTTP Code 429 Too Many Requests
            headers = {
                'User-Agent': 'Eder Martins, teste.com',
                'From': 'zetared@gmail.com'
            }
          
        # Caso não venha nenhum sub reddit, assume news  
        if subreddit in ('', None):
            subreddit = 'news'
        
        # Monta a URL completa e faz o request
        url = self.url_base + '/r/' + subreddit + '/top'
        response=requests.get(url, headers=headers) 
          
        result = []
        # Verificar se a requisiçãp foi realizada com sucesso 
        if response.status_code==200: 
            # Parser com o BeautifulSoup 
            page=BeautifulSoup(response.text,'html.parser')  
            
            # Lista fintrada pela classe 'sitetable'  
            items = page.find(class_='sitetable') 
            
            # Os tópicos ficam têm a classe 'thing'
            for objects in items.findAll(class_='thing'):
                
                #Busca primeiro os likes
                likes_string = objects.findAll(class_='likes')[0].contents[0]
                likes = self._parse_likes_to_float(likes_string)
                #Se não tiver mais likes que o desejado pula
                if likes >= points: 
                    #Busca pelo rank
                    rank_line = objects.findAll('span', class_='rank')
                    rank = rank_line[0].get_text() if len(rank_line) > 0 else ''
                    #Busca pelo título
                    title_line = objects.findAll('a', class_='title')
                    title = title_line[0].get_text() if len(title_line) > 0 else ''
                    #Lê o link para o título
                    title_href = title_line[0].get('href') if title != '' else '/#'
                    title_href = title_href if title_href[0:4] == 'http' else self.url_base + title_href
                    #Busca o link do comentário
                    comments_line = objects.findAll('a', class_='comments')
                    comments_href = comments_line[0].get('href') if len(comments_line) > 0 else '#'
                    #Cada elemento é dict numa lista
                    result.append({
                        "rank": rank, 
                        "likes": likes_string,
                        "subreddit": subreddit, 
                        "title": title, 
                        "comments_href": comments_href, 
                        "title_href": title_href
                    })
        
        return result

if __name__ == "__main__":
    reddit = Reddit()
    print(reddit.sub_reddits_for_telegram("askreddit;worldnews;cats", 500))