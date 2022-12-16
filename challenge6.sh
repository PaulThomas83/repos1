#This is an if and else statement
number5=32
if (($number5 > 32))
then echo "number is greater than 32"
elif (( $number5 < 32 ))
then
echo "number is less than 32"
else
echo "number is 35"
fi


n=2
if (($n==5))
then echo "number is five"
else
echo "number = $n"
fi


if cat challenge6.txt
then "this document exist"
else touch challenge6.txt
fi
