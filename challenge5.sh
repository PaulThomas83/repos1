#!/bin/bash
ps aux

echo "please enter a PID you want to kill"

read PID

for kill in $PID
do
sudo kill $PID
done

echo "$PID killed"
