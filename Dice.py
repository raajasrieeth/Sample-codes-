import random

def rolltheDice():
	'''generates a random number from 1 to 6'''
	return random.randint(1,6)
if __name__ == '__main__':
	print(rolltheDice())