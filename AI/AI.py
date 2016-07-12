import os
import sys
print("Hello, I am a Learning computer")
#Check if name data exists
datacheck=os.path.isfile(".data.dat")
#If the file exists then
if datacheck == 1:
	#Make data file a variable
	with open('.data.dat', 'r') as datafile:
		data=datafile.read()
	name=raw_input("Which user are you (full user name)?: ")
	#If the name is in the datafile and they have a custom file
	if name in data and os.path.isfile(".%s.dat" %name):
		name1=name
	else:
		print("That is not a user. Making a new one...")
		print("What is your name?")
		#Make a new user
		name1 = raw_input("Name(no spaces)(blank for what you entered above): ") or name
		while " " in name1:
			print("No spaces allowed")
			name1 = raw_input("Name(no spaces)(blank for what you entered above): ") or name
		with open('.data.dat', 'a') as datafile:
			datafile.write("\n")
			datafile.write(name)
		#Make a custom use file
		with open(".%s.dat" %name, 'w') as userfile:
			userfile.write("")
			
		#Write user's name to a file
	#Ask for command
	while True:
		print("Hello, %s, how can I help you?" %name1) 
		command=raw_input("Command: ")
		#Check if the command has a program
		programcheck=os.path.isfile("%s.py" %command)
		shellcheck=os.path.isfile("%s.sh" %command)
		javacheck=os.path.isfile("%s.java" %command)
		ccheck=os.path.isfile("%s.c" %command)
		cppcheck=os.path.isfile("%s.cpp" %commnand)
		#Replace space with backslash and space
		command = command.replace(" ", "\\ ")
		#If there is a program then
		if programcheck == 1:
			#Run the program using os.system
			os.system("python %s.py %s" %(command, name1))
			continue
		elif shellcheck == 1:
			os.system("bash %s.sh %s" %(command, name1))
			continue
		elif javacheck == 1:
			os.system("javac %s.java"  %command)
			os.system("java %s" %command)
			os.remove("%s.class" %command)
			continue
                elif cppcheck == 1:
                        os.system("g++ %s.cpp" %command)
                        os.system("g++ %s" %command)
                        os.remove("%s.class" %command)
		else:
			#Ask the user is they would like to make a program
			print("Sorry, I cant do that yet.")
			print("Would you like to make a program for that y)es or n)o?")
			makefile=raw_input()
			if makefile == "y":
				shell=raw_input("Would you like it to be a s)hell script, p)ython, j)ava?, c), or c++?: ")
				if shell == "s":
					os.system("nano %s.sh" %command)
					continue
				elif shell == "p":
					os.system("nano %s.py" %command)
					continue
				elif shell == "j":
					os.system("nano %s.java" %command)
					continue
				elif shell == "c":
					os.system("nano %s.c" %command)
					continue
				elif shell == "c++":
					os.system("nano %s.cpp" %command)
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
	name = raw_input("Name(no spaces): ")
	while " " in name:
		print("No spaces.")
		name = raw_input("Name(no spaces): ")
	#Write user's name to a file
	file = open(".data.dat", 'w')
	file.truncate()
	file.write(name)
	with open(".%s.dat" %name, 'w') as userfile:
		userfile.write("")
	print("Hello, %s, please restart the program."%name)
