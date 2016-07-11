import os
while True:
	command=raw_input("Terminal: ")
	if command == "exit":
		break
	else:
		os.system(command)
