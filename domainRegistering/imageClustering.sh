
#!/bin/bash

{ # try

    rm IMMAGINI/$1/*
    #save your output

} || { # catch
    echo "$1" 
}
echo "$1"

LIST=$(find '/Users/thevault/.virtualenvs/generalTools/domainRegistering/Repository/' -name $1'.png'  )
#echo $LIST



mkdir IMMAGINI/$1
for i in $LIST
do
	
	NOME=$(echo $i| cut -d'/' -f 10)
	echo $NOME".png" , $i
	cp $i IMMAGINI/$1/$NOME".png"
done