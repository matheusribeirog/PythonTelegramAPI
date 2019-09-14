#pyTelegramBotAPI

import telebot
import time

851084690

TOKEN = 'Inserir token aqui'


def escuta(messages):
    for m in messages:
        chatid = m.chat.id
        if(m.text=='promocoes' or m.text=="/promocoes"):
            print(chatid)
            bot.send_message(chatid, """PROMOÇÕES:
            PIZZAS              PREÇOS
            Portuguesa          R$50,00
            Marguerita          R$20,00
            pythonguesa         R$40,00
            /start
            """)


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def comando_teste(menssagem):
    print(menssagem.from_user.first_name)
    bot.reply_to(menssagem,'Olá '+menssagem.from_user.first_name+""" Seja Bem vindo ao Bot da Pizzaria TecPizzas.
    Utilize o menu abaixo:
    Promoções: /promocoes
    Comprar: /comprar
    Cardápio: /cardapio
    """)

@bot.message_handler(commands=['cardapio'])
def cardapio(menssagem):
    print(menssagem.from_user.first_name)
    bot.reply_to(menssagem,"""Cardápio:
            PIZZAS              PREÇOS
            Portuguesa          R$50,00
            Marguerita          R$20,00
            pythonguesa         R$40,00
            MENU:
            /start
            """)

bot.set_update_listener(escuta) #Quando o usuário escrever algo ele chama a função 
bot.polling()


while True: # Don't let the main Thread end.
    pass