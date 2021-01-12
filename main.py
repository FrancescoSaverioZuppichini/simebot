from typing import Any, List
import telebot
from random import choice

TOKEN = "1524901568:AAHPPTHQ6G0DpPS1ewokJC0G8_vUvjc8WZc"


class RandomList(List):
    def random(self) -> Any:
        return choice(self)


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

@bot.message_handler(regexp="^sime.+dove.+sei")
def function_name(message):
    username =message.from_user.username
    msgs = RandomList([f"Ma che domande {username}, sono a Sud!",
                       f"Ma come {username}. Sto andando a sud!"])
    bot.reply_to(message, msgs.random())

@bot.message_handler(regexp="dario|oirad")
def function_name(message):
    msgs = RandomList(["Dario l'hai aperto il fusto?",
                       "Ma quante ne metti giu dario?"])
    bot.reply_to(message, msgs.random())

bot.polling()
