clear

echo "You are about to access the restricted owners panel (y-yes n-no)"
read ans
if [ $ans = 'y' ]
then
echo "Okay"
else
echo "goodbye"
exit
fi
echo "Please enter your owners id"
read pass
if [ $pass = '1812' ] 
then
echo "Welcome Nathan"
elif [ $pass = '1218' ]
then
echo "Welcome Gy"
else
echo "Incorrect"
exit 

  fi
echo "What would you like to view?"
read view
if [ $view = 'users' ]
then
echo $1
else
echo "Bye for now!!!!!"
exit
fi

