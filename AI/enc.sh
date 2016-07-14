echo "Would you like to encrypt a password"
read ans
if [ $ans = 'y' ]
then
echo "Enter your name: "
read name1
sleep 2
echo "Enter your password: "
read pass
sleep 1
echo $pass >> $name1.txt
openssl enc -in $name1.txt -out $name1.enc -e -aes256 -k symmetrickey
rm $name1.txt
else
echo "Goodbye"
exit
fi
