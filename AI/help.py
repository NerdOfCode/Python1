import os
print("Below are the possible commands:")
ls=os.system("ls")
ls=ls.replace(".py","")
print(ls)
