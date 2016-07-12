import os
print "Enter the file: "
print "NOTE: file search automatically searches .py"
find = raw_input()
os.system("find %s.py" %find)

