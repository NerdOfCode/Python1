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
<<<<<<< HEAD
if [ $pass = '1812' ]  
then
echo "Welcome Nathan"

elif [ $pass = '1218' ]

=======
pass=$(echo $pass | md5)
if [ $pass = '78447e5802a3ca1b35653282d9d53589' ] 
then
echo "Welcome Nathan"
elif [ $pass = 'efb632bb211e02dc56d4be50774c70df' ]
>>>>>>> ead6ad07b46ed9b30ce960b5bf1c2c3938bf3d26
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
echo "No support"
exit
fi
