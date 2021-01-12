from typing import Any, List
import telebot
from random import choice

TOKEN = "1524901568:AAHPPTHQ6G0DpPS1ewokJC0G8_vUvjc8WZc"


class RandomList(List):
    def random(self) -> Any:
        return choice(self)


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

@bot.message_handler(regexp="poesia")
def function_name(message):
    msgs = RandomList(["Ei fu. Siccome immobile,
Dato il mortal sospiro,
Stette la spoglia immemore
Orba di tanto spiro,
Così percossa, attonita
La terra al nunzio sta,

Muta pensando all’ultima
Ora dell’uom fatale;
Nè sa quando una simile
Orma di piè mortale
La sua cruenta polvere
A calpestar verrà.

Lui folgorante in solio
Vide il mio genio e tacque;
Quando, con vece assidua,
Cadde, risorse e giacque,
Di mille voci al sonito
Mista la sua non ha:

Vergin di servo encomio
E di codardo oltraggio,
Sorge or commosso al subito
Sparir di tanto raggio:
E scioglie all’urna un cantico
Che forse non morrà.

Dall’Alpi alle Piramidi,
Dal Manzanarre al Reno,
Di quel securo il fulmine
Tenea dietro al baleno;
Scoppiò da Scilla al Tanai,
Dall’uno all’altro mar.

Fu vera gloria? Ai posteri
L’ardua sentenza: nui
Chiniam la fronte al Massimo
Fattor, che volle in lui
Del creator suo spirito
Più vasta orma stampar.

La procellosa e trepida
Gioia d’un gran disegno,
L’ansia d’un cor che indocile
Serve, pensando al regno;
E il giunge, e tiene un premio
Ch’era follia sperar;

Tutto ei provò: la gloria
Maggior dopo il periglio,
La fuga e la vittoria,
La reggia e il tristo esiglio:
Due volte nella polvere,
Due volte sull’altar.

Ei si nomò: due secoli,
L’un contro l’altro armato,
Sommessi a lui si volsero,
Come aspettando il fato;
Ei fe’ silenzio, ed arbitro
S’assise in mezzo a lor.

E sparve, e i dì nell’ozio
Chiuse in sì breve sponda,
Segno d’immensa invidia
E di pietà profonda,
D’inestinguibil odio
E d’indomato amor.

Come sul capo al naufrago
L’onda s’avvolve e pesa,
L’onda su cui del misero,
Alta pur dianzi e tesa,
Scorrea la vista a scernere
Prode remote invan;

Tal su quell’alma il cumulo
Delle memorie scese!
Oh quante volte ai posteri
Narrar se stesso imprese,
E sull’eterne pagine
Cadde la stanca man!

Oh quante volte, al tacito
Morir d’un giorno inerte,
Chinati i rai fulminei,
Le braccia al sen conserte,
Stette, e dei dì che furono
L’assalse il sovvenir!

E ripensò le mobili
Tende, e i percossi valli,
E il lampo de’ manipoli,
E l’onda dei cavalli,
E il concitato imperio,
E il celere ubbidir.

Ahi! forse a tanto strazio
Cadde lo spirto anelo,
E disperò: ma valida
Venne una man dal cielo,
E in più spirabil aere
Pietosa il trasportò;

E l’avviò, pei floridi
Sentier della speranza,
Ai campi eterni, al premio
Che i desidéri avanza,
Dov’è silenzio e tenebre
La gloria che passò.

Bella Immortal! benefica
Fede ai trionfi avvezza!
Scrivi ancor questo, allegrati;
Chè più superba altezza
Al disonor del Golgota
Giammai non si chinò.

Tu dalle stanche ceneri
Sperdi ogni ria parola:
Il Dio che atterra e suscita,
Che affanna e che consola,
Sulla deserta coltrice
Accanto a lui posò."])
    bot.reply_to(message, msgs.random())


bot.polling()
