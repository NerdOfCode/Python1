import os
print("What program would you like to change(complete filename)?")
os.system("ls")
file=raw_input()
file=file.replace(" ", "\\ ")
os.system("nano %s" %file)
