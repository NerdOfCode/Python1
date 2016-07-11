import os
print("What would you like to delete?")
os.system("ls")
delete=raw_input()
print("Are you sure you want to delete %s y)es or n)o?" %delete)
YesNo=raw_input()
if YesNo == "y":
	os.system("rm %s.py" %delete)
else:
	print("Okay.")
