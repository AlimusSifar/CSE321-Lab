#!/bin/bash
function sub {
    num1=$1
    num2=$2
    let "ret=num1-num2"
    return $ret
}

function add {
    num1=$1
    num2=$2
    let "ret=num1+num2"
    return $ret
}

function mul {
    num1=$1
    num2=$2
    let "ret=num1*num2"
    return $ret
}

read -p 'Enter first number: ' a
read -p 'Enter second number: ' b
read -p 'Enter third number: ' c

if [[ a -gt b ]]; then
    sub $a $b
    echo $?
fi

if [[ c -lt b ]]; then
    add $b $c
    echo $?
fi

if [[ b -eq c ]]; then
    mul $b $c
    echo $?
fi
