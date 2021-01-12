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


@bot.message_handler(regexp="^sime.+cosa.+fai")
def function_name(message):
    msgs = RandomList(["E come stasera cosa faccio, prendo il sud",
                       "Dopo westeros!"])
    bot.reply_to(message, msgs.random())


@bot.message_handler(regexp="dario|oirad")
def function_name(message):
    msgs = RandomList(["Dario l'hai aperto il fusto?",
                       "Ma quante ne metti giu dario?"])
    bot.reply_to(message, msgs.random())


bot.polling()
