#!/bin/bash
declare -a array

read -p "Enter number of input: " input

echo "Enter values"
for ((i=0; i < input; i++)) do
    read x
    array[$i]=$x
done

for ((i = 0; i < input; i++)); do
    for ((j = 0; j < input - i - 1; j++)); do
        if [ ${array[j]} -gt ${array[$((j + 1))]} ]; then
            temp=${array[j]}
            array[$j]=${array[$((j + 1))]}
            array[$((j + 1))]=$temp
        fi
    done
done

echo ${array[*]}
