import sys
name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
        data=datafile.read()
if "Favorite Number: " in data:
  for line in data.splitlines():
    if "Favorite Number: " in line:
        line1=line
        break
  color=line1.split("Color: ", 1)[1]
  print("Hello, %s, your favorite number is %s" %(name, color))
elif "Favorite Number: " not in data:
  print("Hello, %s." %name)
  color=raw_input("What is your favorite Number?: ")
  with open('.%s.dat' %name, 'a') as datafile:
    datafile.write("Favorite Numer: %s" %color)
    datafile.write("\n")



