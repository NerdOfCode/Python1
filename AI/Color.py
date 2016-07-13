name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
		data=datafile.read()
if "Favorite Color: " in data:
  lines=datafile.readlines()
  data=lines[1]
  color=data.split("16",1)[1]
  print("Hello, %s, your favorite color is: %s" %(name, color))
else:
  print("Hello, %s." %name)
  color=raw_input("What is your favorite color?: ")
  with open('.%s.dat' %name, 'w') as datafile:
    datafile.write("Favortie Color: %s" %color)
    datafile.write("\n")
