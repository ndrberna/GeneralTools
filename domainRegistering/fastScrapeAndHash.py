import sys
import os
sys.path.append("/Users/thevault/.virtualenvs/generalTools/lib/python2.7/site-packages") # go to parent dir
sys.path.append("/Users/thevault/.virtualenvs/generalTools/domainRegistering") # go to parent dir
from  scrapeSimhashLib import *
import itertools
import pickle 
import sys

def text2tag(text):
    
    soup = BeautifulSoup(text, 'lxml')
    output=str([tag.name for tag in soup.find_all()])

    return output


try:

	
	data = sys.stdin.readlines()
	
	print pickle.dumps(tag2hash(text2tag(' '.join(data))))
	
except:

	print "errore"

