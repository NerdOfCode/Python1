import sys
name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
	data=datafile.read()
	lines=datafile.readlines()
if "Favorite Color:" in data:
  print(data)
  line1=lines[0]
  color=line1.split("16",1)[1]
  print("Hello, %s, your favorite color is: %s" %(name, color))
elif "Favorite Color:" not in data:
  print("Hello, %s." %name)
  color=raw_input("What is your favorite color?: ")
  with open('.%s.dat' %name, 'w') as datafile:
    datafile.write("Favorite Color: %s" %color)
    datafile.write("\n")
