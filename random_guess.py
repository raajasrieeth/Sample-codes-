import random

def generator():
	try:
		lower = int(input("Enter a lower value\t"))
		upper = int(input("Enter a upper value\t"))
		if upper-lower >= 3:
			pick = random.randint(lower,upper)
			x = True
			while x: 
				userChoice = int(input("Try guessing the number\t"))
				if userChoice == pick:
					print("Wow You guessed it !")
					x = False
				elif userChoice >= pick:
					print("It is greater.")
				else:
					print("It is lesser")

			print("Thanks for playing!\t")
		else:
			print("Enter a decent range!")
	except ValueError or TypeError:
		print("Enter a valid number range!!")

generator()	
