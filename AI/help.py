import os
from os import listdir
print("Below are the possible commands:")
ls=os.listdir()
ls=ls.replace(".py","")
print(ls)
