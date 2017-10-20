# comando yupooAnalysis url key

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

def linkExtract(soup):

	for link in soup.find_all('a'):
		if key in link.get('href'):
			new_link=link.get('href')
			
			if new_link not in linkPool:
				linkPool.append(new_link)

def imageExtract(url,soup):
	for link in soup.find_all('img'):
		
		if link.get('src') and key in link.get('src') and ("square" in link.get('src')):

			urlBig=link.get('src').replace("square","big")
			print url,",",urlBig,",",image2String(urlBig),",",qrCode2string(urlBig)

		if link.get('src_data')  and key in link.get('src_data') and ("square" in link.get('src_data')):

			urlBig=link.get('src_data').replace("square","big")
			print url,",",urlBig,",",image2String(urlBig),",",qrCode2string(urlBig)

		if link.get('data-src')  and key in link.get('data-src') and ("square" in link.get('data-src')):

			urlBig=link.get('data-src').replace("square","big")
			print url,",",urlBig,",",image2String(urlBig),",",qrCode2string(urlBig)
		
def image2String(url):
    
    urllib.urlretrieve(url, "inputIMG"+key+".jpg")
    grayImage = []
    grayImage += ('convert', "inputIMG"+key+".jpg")
    grayImage += ('-resize', '400%')
    grayImage+=('-sigmoidal-contrast','20')
    grayImage += ('-type', 'Grayscale','input'+key+'.tif')
    proc = subprocess.Popen(grayImage, stderr=subprocess.PIPE)
    status = proc.wait()
    error_string = proc.stderr.read()
    proc.stderr.close()
    	
    return pytesseract.image_to_string(Image.open('input'+key+'.tif')).strip('\n')		



def qrCode2string(url):
	#Estrazione QRCode
	urllib.urlretrieve(url, "inputCode"+key+".jpg")
	QRImage = []
	QRImage += ('zxing','--try-harder', "inputCode"+key+".jpg")
	proc = subprocess.Popen(QRImage, stdout=subprocess.PIPE)
	status = proc.wait()
	error_string2 = proc.stdout.read()
	proc.stdout.close()
	return(error_string2.strip('\n'))
	#Fine Estrazione QRCode


linkPool=[]
linkPool.append(url)
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# analisi del primo livello di yuppo
imgExtract(soup)

for url in linkPool:
	try:
		print url
		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, "html.parser")
		
		linkExtract(soup)
		print url
		imageExtract(url,soup)
		
	except:
		pass




