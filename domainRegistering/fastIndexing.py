import sys
import os
sys.path.append("/Users/thevault/.virtualenvs/generalTools/lib/python2.7/site-packages") # go to parent dir
sys.path.append("/Users/thevault/.virtualenvs/generalTools/domainRegistering") # go to parent dir
from  scrapeSimhashLib import *
import pickle
import itertools
import sys

import pickle 
data={}
input_data = sys.stdin.readlines()


print "------------------------------------------------------"
print "FAST INDEXING"
testo=''.join(input_data)
#print testo
for i in testo.split(",,,,,"):
	try:
		key=i.split("</key>")[0].split("<key>")[1]
		print "KEY:",key
		hash_value=i.split("</value>")[0].split("<value>")[1]
		#print "SEQUENZA PICKLE:",hash_value
		data[key]=pickle.loads(hash_value)
		print "HASH" +str(pickle.loads(hash_value).value)
	except:
		print ""
		pass


print "DIZIONARIO:"
for i,j in data.items():

	print i,j.value

metadata={}
date="2017-09-22"
index=createHashIndex(data,64,2)
# numero di bit di differenza tollerati
print "bucket: " + str(index.bucket_size())
print "RICERCA CLUSTER"
result=findCLusters(data,index)
print result

print "Numero di elementi" + str(len(data))
#printClusters(result,data,"Fast",metadata,date, 1,700)


filehandler = open("IndexHashDirectDomain"+date, 'w') 
pickle.dump(index, filehandler)
filehandler = open("DataHashDirectDomain"+date, 'w') 
pickle.dump(data, filehandler)