import os
with open('data.dat', 'r') as datafile:
	name=datafile.read()
pwd=os.getcwd()
while True:
	command=raw_input("%s:%s$ " % (name, pwd))
	if command == "exit":
		break
	else:
		os.system(command)
