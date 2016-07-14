import sys
name=sys.argv[1]
with open('.%s.dat' %name, 'r') as datafile:
        data=datafile.read()
if "Favorite Number:" in data:
  for line in data.splitlines():
    if "Favorite Number:" in line:
        line1=line
        break
  number=line1.split("Favorite Number: ", 1)[1]
  print("Hello, %s, your favorite number is %s" %(name, number))
elif "Favorite Number:" not in data:
  print("Hello, %s." %name)
  number=raw_input("What is your favorite Number?: ")
  with open('.%s.dat' %name, 'a') as datafile:
    datafile.write("Favorite Numer: %s" %number)
    datafile.write("\n")



