#input is the number to add up to
#inpu2 is the number to multiply to
#x is the smallest possible answer
#y is the biggest possible answer
input=raw_input("Enter the number to add up to: ")
input2=raw_input("Enter the number to multpily to: ")
input=int(input)
input2=int(input2)
print("")
#Get min and max numbers
x = raw_input("Min number(can be a negative): ")
y = raw_input("Max number: ")
#Convert to int
x = int(x)
y = int(y)
num1=x
num2=x
print"Solving",
#While the answers don't don't work
while num1+num2!=input or num1*num2!=input2:
	num1=num1+1
	num2=num2
	print".",
	if num1+num2==input and num1*num2==input2:
		print("")
		print("The numbers are: ")
		print(num1)
		print("and: ")
		print(num2)
	elif num1>=y and num2<=y:
		num2=num2+1
		num1=x
		continue
