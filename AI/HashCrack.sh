#/bin/bash
#Only works with numbers
#Set var to hash
echo "Enter hash you want to crack:"
read var
number=0
hashtest=$(echo $number | md5)
while True
do
	((number++))
	hashtest=$(echo $number | md5)
	echo $number
	if [ $hashtest == var ]
	then
		echo "Your number is: $number"
		exit
	fi
done
