#!/bin/bash
read -p "Enter an integer: " num

if [ $(($num%10)) -eq 0 ]; then
   if [[ $(($num%4)) -ne 0 || $(($num%5)) -ne 0 ]]; then
       echo "Rasengan"
   fi
fi

if [[ $(($num%5)) -eq 0 || $(($num%6)) -eq 0 ]]; then
    if [[ $(($num%30)) -ne 0 ]]; then
        echo "Oodama Rasengan"
    fi
fi

if [[ $(($num%5)) -eq 0 && $(($num%6)) -eq 0 ]]; then
    echo "Rasen Shuriken"
fi
