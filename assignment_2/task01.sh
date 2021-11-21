#!/bin/bash
sum=0

echo "10 integers"
for ((i=0; i < 5; i++)) do
    read x

    if [ $(($x%2)) -eq 0 ]; then
        if [ $(($x%8)) -ne 0 ]; then
            let "sum += x"
        fi
    fi
done

ans="the sum is $sum"
echo $ans
