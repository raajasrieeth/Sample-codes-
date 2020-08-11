import numpy
from functools import lru_cache
import math
from functools import reduce

@lru_cache(maxsize=2)
def multiplier_basic(*args):
	'''multiiplies all provided numbers'''
	try:
		result = 1 
		for number in args:
			result *= float(number)
		return result

	except TypeError:
		return "Enter numbers!"
def multiplierV2(*args):
	'''uses numpy.prod to return the multiplication'''
	return numpy.prod(args)
#method 3:lambdas:

def multiplierV3(*args):
	'''uses the lambda and reduce function	--> Apply a function of two arguments cumulatively to the items of a sequence, 
	from left to right, so as to reduce the sequence to a single value. 
	For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
	 If initial is present, it is placed before the items of the sequence in the calculation, and serves as a default
	  when the sequence is empty.'''
	result = reduce((lambda x,y:x*y) , args)
	return result	

print(multiplier_basic(1,2,3))

print(multiplierV2(1,2,3,4))

print(multiplierV3(1,2,3,4,5,))

