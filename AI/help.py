import os
from os import listdir
print("Below are the possible commands:")
pwd=os.getcwd()
ls=os.listdir(pwd)
for file in ls:
   if file == "AI.py":
      continue
   if ".py" in file:
      file=file.replace(".py","")
   elif ".sh" in file:
      file=file.replace(".sh","")
   elif ".java" in file:
      file=file.replace(".java", "")
   elif ".c" in file:
      file=file.replace(".c", "")
   elif ".cpp" in file:
      file=file.replace(".cpp", "")
   else:
      continue
   print "%s;" %file,
