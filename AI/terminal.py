import os
import sys
name=sys.argv[1]
pwd=os.getcwd()
while True:
	command=raw_input("%s:%s$ " %(name, pwd))
	if command == "exit":
		break
	else:
		os.system(command)
