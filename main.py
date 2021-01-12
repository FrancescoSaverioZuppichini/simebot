from typing import Any, List
import telebot
from random import choice

TOKEN = "1524901568:AAHPPTHQ6G0DpPS1ewokJC0G8_vUvjc8WZc"


class RandomList(List):
    def random(self) -> Any:
        return choice(self)


with open('./poesia.txt', 'r', encoding='utf8') as f:
    poem = f.read()

with open('./quotes.txt', 'r', encoding='utf8') as f:
    quotes = RandomList(f.readlines())

bot = telebot.TeleBot(TOKEN, parse_mode='MARKDOWN')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Sono simebot!")


@bot.message_handler(regexp="^sime.+(cosa|che).+fai")
def function_name(message):
    username = message.from_user.username
    msgs = RandomList(["E come cosa faccio, prendo il sud",
                       f"Ma secondo te {username}? Invado il sud!"])
    bot.reply_to(message, msgs.random())


@bot.message_handler(regexp="^sime.+dove.+(sei|vai)")
def function_name(message):
    username = message.from_user.username
    msgs = RandomList([f"Sto qua sto, che voi fa? Me voi da' 'na testata ne li cojoni?",
                       f"Ma come {username}. Sto andando a sud!"])
    bot.reply_to(message, msgs.random())


@bot.message_handler(regexp="dario|oirad")
def function_name(message):
    msgs = RandomList(["Dario ma l'hai cambiato il fusto?",
                       "Ma quante ne metti giu Dario?", 
                       "Vergognati Dario"])
    bot.reply_to(message, msgs.random())


@bot.message_handler(regexp="^sono.+(triste|demotivato|depresso)")
def function_name(message):
    msg = f"Spero che questa frase ti faccia sentire forte come quando conquisto il sud. {quotes.random()}"
    bot.reply_to(message, msg)

@bot.message_handler(regexp="sime{3}")
def function_name(message):
    username = message.from_user.username
    msgs = RandomList(["Voglio sentire che pushi e stai venendo a dare una mano, del resto non me ne frega un cazzo",
                       "Io non la volevo giocare 'sta mappa"
                        ])
    bot.reply_to(message, msgs.random())

@bot.message_handler(regexp="^sime.+poesia")
def function_name(message):
    bot.reply_to(message, poem)


bot.polling()
