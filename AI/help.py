import os
from os import listdir
print("Below are the possible commands:")
pwd=os.getcwd()
ls=os.listdir(pwd)
for file in ls and file != "data.dat":
   file=file.replace(".py","")
   print file
