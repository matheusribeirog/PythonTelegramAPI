#pip install pyTelegramBotAPI

import telebot
import time

TOKEN = 'TOKEN AQUI'


def escuta(messages):
    for m in messages:
        chatid = m.chat.id
        if(m.text=='promocoes' or m.text=="/promocoes"):
            print(chatid)
            bot.send_message(chatid, """PROMOÇÕES:
            PIZZAS              PREÇOS
            Portuguesa          R$50,00
            Marguerita          R$20,00
            Calabresa           R$40,00
            Chocolight          R$45,00
            Hot Dog             R$25,00
            Doce Leite          R$40,00
            Frango Catu         R$67,00
            Mussabresa          R$34,00
            /start
            """)
        if(m.text=='desconto' or m.text=="/desconto"):
            print(chatid)
            bot.send_message(chatid, """Desconto para você:
            PIZZA$              DE$CONTO
            Portuguesa          R$20,00
            Marguerita          R$20,00
            Frango Catu         R$27,00
            Mussabresa          R$24,00
            /start
            """)


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def comando_start(menssagem):
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


while True: # DNão deixa a thread principal morrer
    pass