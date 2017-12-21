# Testo prodotto con il comando bash textClustering.sh 2017-09-08
# https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
# https://github.com/reubano/changanya
import sys
import os
import re
sys.path.append("/Users/thevault/.virtualenvs/generalTools/lib/python2.7/site-packages") # go to parent dir


from bs4 import BeautifulSoup
import urllib2

from simhash import Simhash, SimhashIndex
import requests
import lxml
import itertools
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

def url2tag(url):
    page = open(url)
    soup = BeautifulSoup(page.read(), 'lxml')
    output=str([tag.name for tag in soup.find_all()])
    return output

def meta2tag(url):
    page = open(url)
    soup = BeautifulSoup(page.read(), 'lxml')
    meta = soup.findAll(attrs={"name":"description"})
    output=str([tag for tag in meta])
    return output

def url2tagWeb(url):
    r  = requests.get("http://www."+url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    output=str([tag.name for tag in soup.find_all()])
    return output


def tag2hash(tag):
    return Simhash(get_features(tag))

def createHashIndex(data,d,l):
    objs = [(str(k), v) for k, v in data.items()]
    #index = SimhashIndex(objs, k=2)
    index = SimhashIndex(objs,f=d, k=l)
    return index

def findCLusters(data,index):
    cluster=[]
    result=[]
    for k, v in data.items():
    	#print "INIZIO CON " + str(k)
        if str(k) not in result: # elimino dal cluster 
            near_dups=index.get_near_dups(v)
            cluster.append(near_dups)
            for i in  near_dups:
                result=result+[i]

    return cluster

def compare(a, b):
    return a.distance(b)

def fattoriale(x):
    if x == 0:
        return 1
    else:
        return x * fattoriale(x-1)


def internalSimilarity(cluster,data):
    iterazioni = itertools.combinations(cluster, 2)
    unione=0
    for a, b in iterazioni:
        unione=unione+compare(data[a], data[b])
    return unione


def cohesion(cluster,data):
    medoid=findMedoid(cluster,data)
    cohesion=0
    for i in cluster:
        cohesion+=compare(data[i], data[medoid])** 2
    
    return cohesion

def findMedoid(cluster,data):
    risultati={}
    for i in cluster:
        unione=0
        for j in cluster:
            unione=compare(data[i], data[j])
        risultati[i]=unione

    return min(risultati, key=risultati.get)
        



def evaluateClusters(result,data,min_size,max_size):
    
    separation_tot=0
    cohesion_tot=0
    count=0
    for i in result:
        if (len(i)>min_size) and (len(i)<max_size):

            medoid=findMedoid(i,data)
            cluster_distance=0
            for j in result:
                other=findMedoid(j,data)
                
                cluster_distance=cluster_distance+compare(data[medoid],data[other])
            
            count+=1
            cluster=i
            unione=0
            unione=internalSimilarity(cluster,data)
            
            #print "Cluster: "+str(i)
            # elemento medio del cluster
            #print "Medoid: "+ medoid

            # distanza totale medoid da altri medoid mediata da numero di clusters
            #print "Separation: " + str(cluster_distance/len(result))
            separation_tot+=cluster_distance/len(result)
            #print "Cohesion: " + str(unione/len(i))
            cohesion_tot+=unione/len(i)
    
    return cohesion_tot/len(result), separation_tot

def printClusters(result,data,filename,metadata,date,min_size,max_size):
    filename=filename+".html"
    f = open(filename, 'w')
    count=0
    for i in result:
        if (len(i)>min_size) and (len(i)<max_size):

            medoid=findMedoid(i,data)
            cluster_distance=0
            for j in result:
                other=findMedoid(j,data)
                
                cluster_distance=cluster_distance+compare(data[medoid],data[other])
            
            count+=1
            cluster=i
            unione=0
            unione=internalSimilarity(cluster,data)
			
            #print "Cluster: "+str(i)
            #print "Medoid: "+ medoid
            #print "Separation: " + str(cluster_distance)
            #print "Cohesion: " + str(unione)


            print(str(len(i))) 
            f.write("<style>a:link  { text-decoration: none;}a:visited { text-decoration: none;}figure {  display: inline-block;  margin: 10px;}figure img {    vertical-align: top;}</style>")
            f.write("<h4>Cluster num."+str(count)+" - elements: "+str(len(i))+"</h4>") 
            #f.write("<br />element internal distance: "+str(round(float(unione)/(len(i)),2)))
			#print float(unione)
			#print fattoriale(len(i))
			#print "<br><br><b>Cluster:"+str(count)+" </b>" 
            f.write("<table>")
	        
            for j in i:
	            
		            
                filepath="/Users/thevault/.virtualenvs/generalTools/domainRegistering/IMMAGINI/"+date+"/"+j+".png"
                f.write("<figure>")
                if os.path.isfile(filepath):

                    content=""
                    try:
                        content= metadata[j].split('content="')[1].split('"')[0]
						
                    except:
                        pass
                    f.write("<a title='"+content + "' target=_blank href="+filepath+"><img width='100px' src="+filepath+"></a>")
					
					
                f.write("<figcaption><a target=_blank href=http://www."+j+">"+j+"</a></figcaption>")
                f.write("</figure>")
	            #print metadata[j]
	        
            f.write("<br>")
    f.close()



def printSimpleClusters(result,data,filename,date,min_size,max_size):
    filename=filename+".html"
    f = open(filename, 'w')
    count=0
    for i in result:
        if (len(i)>min_size) and (len(i)<max_size):

            medoid=findMedoid(i,data)
            cluster_distance=0
            for j in result:
                other=findMedoid(j,data)
                
                cluster_distance=cluster_distance+compare(data[medoid],data[other])
            
            count+=1
            cluster=i
            unione=0
            unione=internalSimilarity(cluster,data)
            
            #print "Cluster: "+str(i)
            #print "Medoid: "+ medoid
            #print "Separation: " + str(cluster_distance)
            #print "Cohesion: " + str(unione)


            print(str(len(i))) 
            f.write("<style>a:link  { text-decoration: none;}a:visited { text-decoration: none;}figure {  display: inline-block;  margin: 10px;}figure img {    vertical-align: top;}</style>")
            f.write("<h4>Cluster num."+str(count)+" - elements: "+str(len(i))+"</h4>") 
            #f.write("<br />element internal distance: "+str(round(float(unione)/(len(i)),2)))
            #print float(unione)
            #print fattoriale(len(i))
            #print "<br><br><b>Cluster:"+str(count)+" </b>" 
            f.write("<table>")
            
            for j in i:
                
                    
                filepath="/Users/thevault/.virtualenvs/generalTools/domainRegistering/IMMAGINI/"+date+"/"+j+".png"
                f.write("<figure>")
                if os.path.isfile(filepath):

                    
                    f.write("<a title='"+content + "' target=_blank href="+filepath+"><img width='100px' src="+filepath+"></a>")
                    
                    
                f.write("<figcaption><a target=_blank href="+j+">"+j+"</a></figcaption>")
                f.write("</figure>")
                #print metadata[j]
            
            f.write("<br>")
    f.close()