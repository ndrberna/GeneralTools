import requests,re
from bs4 import BeautifulSoup

from urlparse import urlparse, parse_qs
r = requests.get('http://www.google.com/search', params={"source":"hp","q":"site:cnn.com test","oq":"site:cnn.com london","gs_l":"psy-ab.12...10773.10773.0.22438.3.2.0.0.0.0.135.221.1j1.2.0....0...1.2.64.psy-ab..1.1.135.6..35i39k1.zWoG6dpBC3U"})

soup = BeautifulSoup(r.content,"html.parser")

links = []
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    links.append(item.a['href'])

print(links)