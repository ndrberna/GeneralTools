

sort DomainsRegistered2017-* | uniq > DomainsTotal.txt 
IFS=$'\n' read -d '' -r -a lines < brand_list.txt
STOP=$'\n' read -d '' -r -a stop_sites < stop_list.txt

URL="DomainsTotal.txt"




for i in "${lines[@]}"
do

	for j in "$(grep -E $i $URL )"
	
	do
		
		echo  $j
		for k in "${stop_sites[@]}"
		do
			
			
			if [ "$j" == "$k" ] ; then
	        echo "FOUND"
	    	fi
	    done
	done
done


