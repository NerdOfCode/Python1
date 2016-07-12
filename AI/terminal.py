import os
from AI.py import name1
pwd=os.getcwd()
while True:
	command=raw_input("%s:%s$ " % (name, pwd))
	if command == "exit":
		break
	else:
		os.system(command)
