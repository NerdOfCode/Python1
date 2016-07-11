import sys
brutelist=open("Brute.txt", "wb")
#characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<>,./?;:[]:|'\"\\"
#characters = "1234567890"
desiredPlacesstr=raw_input("How long is the password?: ")
characters=raw_input("What characters are possibly in the password(leave blank for default): ") or "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<>,./?;:[]:|'\"\\"
desiredPlaces=int(desiredPlacesstr)
length=len(characters)
iterations = pow(length, desiredPlaces)


for index in xrange(iterations) :
    number = index

    characterStack = []

    for place in xrange(desiredPlaces) :
        digit = number % length
        characterStack.append(characters[digit])

        number = number / length

	brute=''.join(list(reversed(characterStack)))
	
    print(brute)
	
    brutelist.write("%s" %brute)
    brutelist.write("\n")
