
#!/bin/bash

# FONTE DATI: https://domainpunch.com/tlds/daily.php
# prendere la chiamata dentro la tabella e copiarla dentro il codice inserendo poi l'elemento variabile di start
# il passo di campionamento dei dati è fisso ed è di 1000 elementi.

start=0

DATE=`date +%Y-%m-%d`


while (( start < 130000 ))
do
	echo $start
	
	#curl 'https://domainpunch.com/tlds/daily.php?domains&draw=4&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5Bdir%5D=asc&start='$start'&length=1000&search%5Bvalue%5D=&search%5Bregex%5D=false&zid=1&_=1506067578041' -H 'Cookie: _jsuid=3490766586; _referrer_og=https%3A%2F%2Fwww.google.it%2F; PHPSESSID=1171oua8srb1r3m3dkvu05bl56; _first_pageview=1; _eventqueue=%7B%22heatmap%22%3A%5B%5D%2C%22events%22%3A%5B%5D%7D' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://domainpunch.com/tlds/daily.php' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed >> UrlRegistered$DATE.txt
	
	curl 'https://domainpunch.com/tlds/daily.php?domains&draw=3&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5Bdir%5D=asc&start='$start'&length=1000&search%5Bvalue%5D=&search%5Bregex%5D=false&zid=1&_=1506501803972' -H 'Cookie: _jsuid=3490766586; _referrer_og=https%3A%2F%2Fwww.google.it%2F; PHPSESSID=1171oua8srb1r3m3dkvu05bl56; _first_pageview=1; _eventqueue=%7B%22heatmap%22%3A%5B%5D%2C%22events%22%3A%5B%5D%7D' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://domainpunch.com/tlds/daily.php' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed >> UrlRegistered$DATE.txt


	

	start=$((start + 1000))
done

more  UrlRegistered$DATE.txt |  cut -b2- | tr ',{' '\n,{' | grep -E '^("1":)' | cut -b2- | tr -d '"1":"'  >  DomainsRegistered$DATE.txt
