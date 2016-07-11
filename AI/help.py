import os
from os import listdir
print("Below are the possible commands:")
directory=os.popen("pwd")
ls=os.listdir(pwd)
for file in ls:
   file=file.replace(".py","")
   print file
