# Copyright NerdOfLinux
# You may only modify this for personal use. If you would like to use it for anything else, please contact me.
#Import required libraries
import os
import sys
from random import randint
print("Welcome to the random movie picker.")
print("Your random movies is: ")
#Check if file exists
if os.path.isfile("movies.txt") == False:
	setup=raw_input("Would you like to run the setup y)es or n)o: ")
	if setup == "y":
		os.system("python MoviePicker")
	else:
		print("Ok, exiting.")
		sys.exit()
#Open the file
file=open("movies.txt", "r")
#Check file length
with open('movies.txt') as f:
    length=sum(1 for _ in f)
if length==0:
	print("File blank, please run MoviePicker.py")
	sys.exit()
#Read individual lines
lines=file.readlines()
#Random number
number=randint(0,length-1)
#Use random number as line number
randomline=lines[number]
file.close()
file=open("movies.txt", "w")
#Rewrite everything but the chosen movie
print(randomline)
for line in lines:
	if line!="%s"%randomline:
		file.write(line)
