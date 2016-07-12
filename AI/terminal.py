import os
with open('.data.dat', 'r') as datafile:
	data=datafile.read()
name=raw_input("Which user are you (full user name)?: ")
if name in data and os.path.isfile(".%s.dat" %name):
	name=name
pwd=os.getcwd()
while True:
	command=raw_input("%s:%s$ " % (name, pwd))
	if command == "exit":
		break
	else:
		os.system(command)
