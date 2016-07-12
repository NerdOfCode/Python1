import os
from os import listdir
print("Below are the possible commands:")
pwd=os.getcwd()
ls=os.listdir(pwd)
for file in ls:
   if file == "data.dat" or file == "AI.py":
      continue
   if ".py" and ".sh" not in file:
      continue
   if ".py" in file:
      file=file.replace(".py","")
   elif ".sh" in file:
      file=file.replace(".sh","")
   print "%s;" %file,
