#!/bin/bash
ps aux

echo "please enter a PID you want to kill"

read PID

for kill in $PID
do
sudo kill $PID
done

echo "$PID killed"

#!/bin/bash

# How to show time and date

year=`date +%Y`
month=`date +%m`
day=`date +%d`
hour=`date +%H`
minute=`date +%M`
second=`date +%S`
echo `date`
echo "Current Date: $day-$month-$year"
echo "Current Time: $hour:$minute:$second"
