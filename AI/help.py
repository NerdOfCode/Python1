import os
from os import listdir
print("Below are the possible commands:")
pwd=os.getcwd()
ls=os.listdir(pwd)
for file in ls:
   if file == "data.dat":
      continue
   file=file.replace(".py","")
   print file
