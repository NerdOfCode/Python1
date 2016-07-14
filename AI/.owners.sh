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
read input
pass=$(echo "$input" | openssl enc -e -aes256 -k symmetrickey)
if [ "$pass" = 'Salted__???V+???]?N!X?:z?>' ] 
then
  echo "Welcome Nathan"
elif [ "$pass" = 'Salted__??B???Շp?>???D???1.?' ]
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
