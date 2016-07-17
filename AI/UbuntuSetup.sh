whoami=$(whoami)
if [ "$whoami" != "root" ]
then
  echo "Please run as root"
  exit 0
fi

apt-get install espeak >> /dev/null
