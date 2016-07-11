with open('data.dat', 'r') as datafile:
	name=datafile.read()
feeling=raw_input("How are you today, %s?: " %name)
print("I'm also feeling %s" %feeling)
