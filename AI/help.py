import os
from os import listdir
print("Below are the possible commands:")
directory=os.popen("pwd")
ls=os.listdir(pwd)
ls=ls.replace(".py","")
print(ls)
