
class Powers():
	def __init__(self,num,power):
		self.num=num
		self.power=power
	def expo(self):
		return f"{self.num} to the power of {self.power} is: {self.num**self.power}"
x=float(input("Enter a number"))
y=int(input("Enter the power"))
var=Powers(x,y)
try:
	print(var.expo())
except TypeError:
	print("Enter a number!!")
finally:
	print("done")

#class methods:
class Employee:
	employees=0
	raise_percent=1.05
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
		self.email=fname+'.'+lname+'@sample.com'
		Employee.employees+=1
	@classmethod#applied to the class
	def class_raise_amt(cls,updated_rp):#note cls is NOT a keyword , but as the function runs on the class ,it is an argument
		cls.raise_percent=updated_rp
	@classmethod
	def new_function(cl,val):
		cl.employees+=val#increments the number of the employees by entered arg
	@staticmethod#no class related args, can be used by syntax: classname.functionname(args)
	def func():
		print("Hello,World!")
#now , using these :
Employee.class_raise_amt(1.07)
print(Employee.raise_percent)#now prints updated value
Employee.new_function(7)#adds 7 employees
print(Employee.employees)
#create a class instance:
Tim=Employee("Tim","C",40000)
print(Tim.email)
Employee.func()

#coroutines:
#run a function from another line
import time
def some_func():
	name_of_str="Some long string"
	time.sleep(4)#4 seconds will pass, maybe more
	#now, to NOT execute the above part when the function is called next, but the following code, coroutines are used
	x=True
	while x:
		text=(yield)#yield is a generator, saves ram,etc,generates values on the fly.when used in brackets, conveys to python that
		#it is a coroutine now, runs from the yield statement
		if text in name_of_str:
			print("Yes it is in the string")
		else:
			print("no")
ins_of_some_func=some_func()#instance of function
next(ins_of_some_func)#iteration
ins_of_some_func.send("Name")#checks if in the str, takes 4 sec
ins_of_some_func.send("Some")#executes without any delay

#to end loop:
ins_of_some_func.close()
#*args and **kwargs:
def function_printname(a,b,c,d):
	print(a,b,c,d)#prints values of arguments, to add more arguments:
function_printname("val","val2","val3","val4")#note a new arument cant be passed. So,:
def newfunc(anything,*args,**kwargs):#note *name is the syntax, not, *args and converts arguments to a tuple
#kwargs are keyword  variable length arguments
	print(anything)
	print(args[0])#can be indexed
	for i in args:
		print(f"name of person:{i}")
	for key,value in kwargs.items():
		print(f"{key} is a value {value}")

x="A normal argument"
lst=["Name1","Name2","Name3"]
dicts={"VAl":2,"name":4}

newfunc(x,*lst,**dicts)#syntax *args follow the normal args

#another example:
inp_num=100
lstp=[]

def primes(*args):
	print(*args[3])

for num in range(2,inp_num+1):
	c=0
	for x in range(2,num-1):
		if num%x==0:
			c+=1
	if c==0:
		lstp.append(num)

primes(*lstp)
ls=list(x for x in range(25))#prints numbers from 0 to 24






