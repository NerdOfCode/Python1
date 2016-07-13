import sys
name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
	data=datafile.read()
	lines=datafile.readlines()
if "Favorite Color:" in data:
  color=data
  print("Hello, %s, your favorite color is: %s" %(name, color))
elif "Favorite Color:" not in data:
  print("Hello, %s." %name)
  color=raw_input("What is your favorite color?: ")
  with open('.%s.dat' %name, 'w') as datafile:
    datafile.write(color)
    datafile.write("\n")
