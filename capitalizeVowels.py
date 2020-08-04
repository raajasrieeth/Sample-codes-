from functools import lru_cache 
import time

@lru_cache(maxsize=2)
def translator(userInput):
	'''Translates the vowels in the input and replaces them with another letter.
	a --> z
	e --> y
	i --> x
	o --> w
	u --> v'''
	print("Translating...")
	time.sleep(1)
	translation = " "
	vowels = ["a" ,"e", "i","o","u"]
	for letter in userInput:
		if letter is vowels[0]:
			translation += "z"
		elif letter is vowels[1]:
			translation += "y"
		elif letter is vowels[2]:
			translation += "x"
		elif letter is vowels[3]:
			translation += "w"
		elif letter is vowels[4]:
			translation += "v"
		else:
			translation += letter
	print(f"Translation is as follows:\t{translation}")


translator("aeiou")
translator("aeiou")
# print(translator.__doc__)