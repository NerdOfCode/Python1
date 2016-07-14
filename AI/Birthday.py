import sys
name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
	data=datafile.read()
if "Birthday:" in data:
  for line in data.splitlines():
    if "Birthday" in line:
    	line1=line
    	break
  color=line1.split("Color: ", 1)[1]
elif "Birthday" not in data:
  print("Hello, %s." %name)
  birthday=raw_input("When is your birthday(in numbers)(month/day/year)?: ")
  with open('.%s.dat' %name, 'a') as datafile:
    datafile.write("Birthday: %s" %birthday)
    datafile.write("\n")
