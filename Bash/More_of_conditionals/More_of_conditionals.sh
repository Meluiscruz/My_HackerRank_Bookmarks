#!/bin/bash
read num1
read num2
read num3

if [ $num1 = $num2 -a $num1 = $num3 ] 
then 
echo "EQUILATERAL"
elif [ $num1 = $num2 -o $num1 = $num3 -o $num2 = $num3 ]
then
echo "ISOSCELES"
else 
 echo "SCALENE" 
fi