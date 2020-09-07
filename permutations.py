#use the itertools to show possible permutations

import itertools

def perms():
	'''yield possible permutations'''
	#print(itertools.permutations.__doc__)
	for perm in itertools.permutations('ABCD'):
		print(perm)
		


if __name__=='__main__':
	perms()
# to use: generators to make the job not memory intensive.