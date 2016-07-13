name=sys.argv[1]
with open('%s.dat' %name, 'r') as datafile:
  datafile.write("Favortie Color: ")
  
print("Hello, %s." %name)
color=raw_input("What is your favorite color?: ")
with open('%s.dat' %name, 'w') as datafile:
  datafile.write("Favortie Color: ")
