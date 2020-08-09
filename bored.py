import random
import matplotlib.pyplot as plt 
import matplotlib.style

list_of_stuff = [ "bar" , "barh" ,"plot" ,]
lst = []
lsty = []
for i in range(30):
	lst.append(random.randint(0,30))
	lsty.append(random.randint(0,30))
def doSomething():
	'''does some graph'''
	plt.style.use('ggplot')
	c = random.choice(list_of_stuff)
	if c == "plot":
		plt.plot(lst , lsty)
	elif c == "bar":
		plt.bar(lst,lsty)
	elif c == "barh":
		plt.barh(lsty,lst)
	plt.title("plot of randomness")
	plt.xlabel("randomness")
	plt.ylabel("also randomness")
	plt.show()
doSomething()
