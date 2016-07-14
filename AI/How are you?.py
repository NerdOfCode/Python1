import sys
import random
name=sys.argv[1]
feeling=raw_input("How are you today, %s?: " %name)
feelings=['good', 'happy', 'sad', 'cheerful']
random=random.choice(feelings)
if feeling.lower() == random.lower():
	print("I am also feeling %s right now." %random)
else:
	print("Oh. I am feeling %s right now." %random)
