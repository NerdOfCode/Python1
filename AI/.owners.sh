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
pass=$(echo "$input" | openssl dgst -sha512)
if [ "$pass" = '3ebb46cf6d743654d4878631021e416fe59408573c570f38892969642810975e6c5cb80aa35b0e5aa31868914b2673fa0945daeeeac3ffa5a3cdd2c829a570a9' ] 
then
  echo "Welcome Nathan"
elif [ "$pass" = '81ebbf6fd53f040889ee0fecfe7a2e24a339fd8b3163f1a55f25978c19e9348351df0d6a0e65988f7f89c23477d8fb617f5a59868c789569b25799bfe5e0bffd' ]
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
