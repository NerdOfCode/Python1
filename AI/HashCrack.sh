#/bin/bash
#Only works with numbers
#Set var to hash
var=""
number=0
hashtest=$(echo $number | md5)
while True
do
	((number++))
	hashtest=$(echo $number | md5)
	if [ $hashtest == var ]
	then
		echo $number
		exit
	fi
done
