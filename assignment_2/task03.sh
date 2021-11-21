#!/bin/bash
function happy {
    local sum
    local num
    sum=0

    for ((num=$1; num > 0; num/=10)) do
        let "digit = num % 10"
        let "sum += digit ** 2"
    done

    return $sum
}

read -p "Enter a number to check if it is happy: " input

num=$input
res=$num

while [[ $res -ne 1 && $res -ne 4 ]]; do
    happy $res
    res=$?
done

if [ $res -eq 1 ]; then
    echo "$num is happy"

else
    if [ $res -eq 4 ]; then
        echo "$num is not happy"
    fi
fi
