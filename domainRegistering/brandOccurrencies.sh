
#!/bin/bash

# scaricamento incrementale di tutti i domini registrati dal primo settembre
sort DomainsRegistered2017-* | uniq > DomainsTotal.txt 
URL=DomainsTotal.txt


# scaricamento dei soli domini di una giornata
# URL="DomainsRegistered2017-0928"


IFS=$'\n' read -d '' -r -a lines < brand_list.txt
DATE=`date +%Y-%m-%d`

DIR="Repository"

for i in "${lines[@]}"
do
	#echo $i

	OUTPUT="$(grep -E $i $URL )"
	
	for j in ${OUTPUT}
	do
		

		if [ ! -d $DIR ]
		  then mkdir $DIR
		fi
		if [ ! -d $DIR/$i ]
		  then mkdir $DIR/$i
		fi
		if [ ! -d $DIR/$i/$j/ ]
		  then mkdir $DIR/$i/$j
		fi
		if [ ! -d $DIR/$i/$j/Screenshots ]
		  then mkdir $DIR/$i/$j/Screenshots
		fi
		
		if [ ! -d $DIR/$i/$j/Code ]
		  then mkdir $DIR/$i/$j/Code
		fi

		if [ ! -d $DIR/$i/$j/Whatruns ]
		  then mkdir $DIR/$i/$j/Whatruns
		fi

		sem -j+0 --no-notice  curl  --connect-timeout 10  -s -L $j  > $DIR/$i/$j/Code/$DATE.html
		sem -j+0 --no-notice  python screenshotANDtechnologies.py "http://www."$j $DIR/$i/$j/Screenshots/$DATE.png $DIR/$i/$j/Whatruns/$DATE.html
	done
	sem --wait
done

pkill -f firefox