import os
import sys

print "Hello what is your nickname"
datacheck=os.path.isfile("nick.data")

if datacheck == 1:
 with open('nick.data', 'r') as datafile:
  name=datafile.read()
print "Hello %s, you already are registered with your nickname!" %name
   else:
        print "I dont know currently know your nickname!"
        print "Enter it now: " 
        name = raw_input()
        print "Saving %s, as your nickname!" %name
