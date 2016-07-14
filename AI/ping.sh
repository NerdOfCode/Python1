echo "What would you like to ping?"
echo "NOTE: automaticaly adds "".com"" to the end of your web address "
read address
ping -c 10 $address.com
