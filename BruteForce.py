# You may only modify this for personal use. If you would like to use it for anything else, please contact me.
#You may NOT use this for any illegal purposes.
# I am not responsible for any damage caused by this.
import sys
brutelist=open("Brute.txt", "wb")
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
