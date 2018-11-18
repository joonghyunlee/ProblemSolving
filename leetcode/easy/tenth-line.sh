#!/bin/bash

cat > file.txt << EOF
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
EOF

## Solution 1
head -n 10 file.txt | tail -n +10

## Solution 2
COUNT=0
while read LINE
do
    COUNT=$((COUNT+1))
    if [ $COUNT -eq 10 ]
    then
        echo $LINE
        break
    fi
done < file.txt

## Solution 3
awk 'NR == 10' file.txt

rm -f file.txt
