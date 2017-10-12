#!/bin/bash

# comando bash textClustering.sh 2017-09-08

# APRE IL FILE DOMAINS della giornata $1  


echo "$1"
LIST=$(find '/Users/thevault/.virtualenvs/generalTools/domainRegistering/Repository/' -name $1'.html'  )
#echo $LIST
# mkdir HTML/BRAND/$1
mkdir HTML/$1


for i in $LIST
do
	if [[ $i == *"Code"* ]]; then
	  
	  NOME=$(echo $i| cut -d'/' -f 10)
	  #echo $i, $NOME".html" 
	  #cp $i HTML/BRAND/$1/$NOME".html"
	  cp $i HTML/$1/$NOME".html"
	  
	fi
	
done