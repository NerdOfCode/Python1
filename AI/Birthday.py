import sys
import datetime
name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
	data=datafile.read()
if "Birthday:" in data:
  for line in data.splitlines():
    if "Birthday" in line:
    	line1=line
    	break
  birthday=line1.split("Birthday: ", 1)[1]
  date=time.strftime("%m/%d")
  if date == birthday:
  	print("Happy birthday!")
  else:
  	print("Your birthday is on %s" %birthday)
elif "Birthday" not in data:
  print("Hello, %s." %name)
  birthday=raw_input("When is your birthday(in numbers)(month/day)?: ")
  with open('.%s.dat' %name, 'a') as datafile:
    datafile.write("Birthday: %s" %birthday)
    datafile.write("\n")
