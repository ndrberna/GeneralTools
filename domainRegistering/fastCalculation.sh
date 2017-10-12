
#!/bin/bash
declare -A  arr
URL="test_domain.txt"
OUTPUT="$(more $URL )"

ref_array() {
    local varname="$1"
    local export_as="$2"
    local code=$(declare -p "$varname")
    echo ${code/$varname/$export_as}
}

dump() {
    eval $(ref_array "$1" array)
    local key

    for key in "${!array[@]}"; do
        printf "<key>%s</key><value>%s</value>,,,,," "$key" "${array[$key]}"
        
    done
}

start=`date +%s`



for j in ${OUTPUT}
	do
		
        data=$(sem -j+0 --no-notice  curl $j --connect-timeout 2 --max-time 10 | python fastScrapeAndHash.py $j )
		
        arr[$j]=$data
        sem --wait
        
	done
	#
wait    
end=`date +%s`
runtime=$((end-start))

startIndexing=`date +%s`
dump arr |  python fastIndexing.py
endIndexing=`date +%s`
runtimeIndexing=$((endIndexing-startIndexing))
echo "TEMPO DI DOWNLOAD:" $runtime
echo "TEMPO DI INDICIZZAZIONE:" $runtimeIndexing