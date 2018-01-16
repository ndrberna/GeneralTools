from bs4 import BeautifulSoup

import urllib
import requests

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os
import sys
import subprocess

url = sys.argv[1]
key= sys.argv[2]

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

linkPool=[]
linkPool.append(url)
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

print soup.find_all('div')

