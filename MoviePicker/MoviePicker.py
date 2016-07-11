# Copyright Gy Ben-Yaakov
# You may only modify this for personal use. If you would like to use it for anything else, please contact me.
#Import required libraries
import os
import sys
#If file exists, get the length
if os.path.isfile("movies.txt"):
	with open('movies.txt') as f:
	    length=sum(1 for _ in f)

#If movies.txt exists and has content
if os.path.isfile("movies.txt") and length>0:
	print("A movies file already exists.")
	#Ask to overwrite
	rmfile=raw_input("Would you like to overwrite the file y)es or n)o: ")
	#If they don't want to overwrite
	if rmfile != "y":
		#Ask to run MoviePicker2
		run=raw_input("Would you like to randomly choose a movie y)es or n)o: ")
		if run == "y":
			os.system("python MoviePicker2.py")
			sys.exit()
		else:
			#Exit
			print("Ok, exiting.")
			sys.exit()
	
print("Welcome to the random  movie picker setup.")
print("The program will ask you for all the movies you have and randomly choose one. Type 'done' when you have listed al your movies")
#Creates file if it doesn't exist
file=open("movies.txt", "w")
#Set movienum to 1
movienum=1
#Ask and write movies
movie=raw_input("Please enter movie %i: " %movienum)
file.write(movie)
#Add new line to file
file.write("\n")
movienum=movienum+1
#While the movie is not done
while movie != "done":
	movie=raw_input("Please enter movie %i: " %movienum)
	if movie == "done":
		#If the movie is done, then don't write it to the file
		continue
	else:
		#Else write the name to a file
		file.write(movie)
		file.write("\n")
		movienum=movienum+1
else:
	#Close the file
	file.close()
	os.system("python MoviePicker2.py")
	sys.exit()