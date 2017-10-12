# COMANDO bash brandDomain.sh armani

#!/bin/bash

cd $1
for i in * ; do
  if [ -d "$i" ]; then
    count=$(ls -l $i/Screenshots/* | grep -v ^l | wc -l)
    echo "$i,$count"
  fi
done






