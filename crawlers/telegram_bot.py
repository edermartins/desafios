import telebot
from scraper.reddit import Reddit
from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Comandos: /NadaPraFazer subredditA;subredditB;...')

@bot.message_handler(commands=['teste'])
def send_help(message):
    bot.reply_to(message, '*Eder*: [LinkedIn](http://www.linkedin.com/in/edermartins)', parse_mode='Markdown')

@bot.message_handler(commands=['NadaPraFazer'])
def send_trends(message):
    text = message.text.split()
    if len(text) > 2:
        bot.reply_to(message, 'Não use múltiplas linhas ou caracteres especiais')
    else:
        reddit_scraper = Reddit()
        posts = reddit_scraper.sub_reddits_for_telegram(text[1])
        for post in posts:
            bot.send_message(message.chat.id, post['line'], parse_mode='Markdown', disable_web_page_preview=True)

@bot.message_handler(commands=['NadaPraFazerB'])
def send_trends_b(message):
    text = message.text.split()
    if len(text) > 2:
        bot.reply_to(message, 'Não use múltiplas linhas ou caracteres especiais')
    else:
        reddit_scraper = Reddit()
        posts = reddit_scraper.sub_reddits_for_telegram(text[1])
        for post in posts:
            bot.send_message(message.chat.id, post['post'], parse_mode='Markdown', disable_web_page_preview=True, reply_markup=post['markup'])

bot.polling(none_stop=True)
