print("I am too, whats your favorite number?")

userinput = raw_input("Enter a number: ") 
userinput=int(userinput)

if userinput < 100:
  print("That number is below 100.")
else:
  print("Big number is detected")
