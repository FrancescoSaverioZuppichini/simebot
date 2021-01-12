import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
URL = 'https://www.esserealtop.it/365-frasi-motivazionali-che-ti-cambieranno-la-vita/'

OUT_PATH = './quotes.txt'

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

a_tags = soup.findAll('a')

is_quote = lambda x: "https://twitter.com/share?text" in x['href']
a_tags = filter(is_quote, a_tags)

quotes = list(tqdm(map(lambda x: x.text, a_tags)))
# skip every two (one <a> contains the quote and the next one the "Click to Tweet")
quotes = quotes[::2]

with open(OUT_PATH ,'w', encoding='utf8') as f:
    f.write('\n'.join(quotes))