import os
print("What program would you like to change?")
os.system("ls")
file=raw_input()
file=file.replace(" ", "\\ ")
os.system("nano %s.py" %file)
