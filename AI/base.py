import base64

print "Enter the string you would like to encode: "
userinput = raw_input()
e = base64.b64encode(userinput)
print "%s" %e

