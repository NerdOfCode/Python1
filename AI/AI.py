import os
import sys
print("Hello, I am a Learning computer")
#Check if name data exists
datacheck=os.path.isfile("data.dat")
#If the file exists then
if datacheck == 1:
	#Make data file a variable
	with open('data.dat', 'r') as datafile:
		name=datafile.read()
	#Ask for command
	while True:
		print("Hello, %s, how can I help you?" %name) 
		command=raw_input("Command: ")
		#Check if the command has a program
		programcheck=os.path.isfile("%s.py" %command)
		shellcheck=os.path.isfile("%s.sh" %command)
		javacheck=os.path.isfile("%s.java" %command)
		#Replace space with backslash and space
		command = command.replace(" ", "\\ ")
		#If there is a program then
		if programcheck == 1:
			#Run the program using os.system
			os.system("python %s.py" %command)
			continue
		elif shellcheck == 1:
			os.system("bash %s.sh" %command)
			continue
		elif javacheck == 1:
			os.system("javac %s.sh"  %command)
			os.system("java %s" %command)
			os.remove("%s.class" %command)
			continue
		else:
			#Ask the user is they would like to make a program
			print("Sorry, I cant do that yet.")
			print("Would you like to make a program for that y)es or n)o?")
			makefile=raw_input()
			if makefile == "y":
				shell=raw_input("Would you like it to be a s)hell script or p)ython?: ")
				if shell == "s":
					os.system("nano %s.sh" %command)
					continue
				elif shell == "p":
					os.system("nano %s.py" %command)
					continue
				else:
					print("Error, please try again.")
					continue
			else:
				print("Ok")
				continue
else:
	#Get name
	print("What is your name?")
	name = raw_input("Name: ")
	#Write user's name to a file
	file = open("data.dat", 'w')
	file.truncate()
	file.write(name)
	print("Hello, %s, restarting program."%name)
	os.system("python AI.py")
