import os
pwd=os.getcwd()
while True:
	command=raw_input("%s$ " %pwd)
	if command == "exit":
		break
	else:
		os.system(command)
