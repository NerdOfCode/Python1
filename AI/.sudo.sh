echo "Welcome to the sudoers file!"
echo "Current user is "$1
if [ $1 == 'Nate' ]
then
echo "Youre logged in"
elif [ $1 == 'Gy' ]
then
echo "Youre logged in"
else
echo "Sorry you are not a super user"
exit
fi
clear
echo "Welcome superuser " $1
sleep 3
clear
echo "Would you like to tell me your favorite number for future sudo uses"
read answer
if [ $answer == 'y' ]
then
echo "Enter it now: " 
read numb
echo $numb >> .Numb.dat
echo $1 >> .Numb.dat
echo "______________________________" >> .Numb.dat
else
echo "Okay"
fi
clear
echo "This program is incomplete"
