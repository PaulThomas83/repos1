#!/bin/bash

# script: Ops challenge class 4
# author: Paul Thomas
# date: 1-26-2023
# purpose: conditionals in menu systems

e=y
while [$e = y ]
do

echo "make a selection"
echo "1) hello world"
echo "2) ping self"
echo "3) list ip info"
echo "4) exit"

read a
if [ $a = 1 ] then
echo "hello world"
elif [ $a = 2 ]
     then ping -c 3 127.0.0.1
elif [ $a = 3 ]
    then ifconfig
else [ $a = 4 ]
exit
fi