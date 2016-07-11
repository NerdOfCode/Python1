print "I am too, whats your favorite number?"

userinput = raw_input("Your favorite number is ") 
userinput=int(userinput)

if userinput < 100:
  print "That number is below 100"
else:
  print "That is one big number!"
