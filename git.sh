cd Git
git pull origin master
echo "Would you like to ssh y)es or n)o?"
read yesno
if [ $yesno = "y" ]
then
	ssh git@ec2-54-215-190-29.us-west-1.compute.amazonaws.com
else
	echo "Okay."
	exit
fi
