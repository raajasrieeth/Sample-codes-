import math
class Day():
	'''tells which day a date falls on '''
	def __init__(self,date , month , year):
		self.date = date
		self.month = month
		self.year = year
	def tellDay(self):
		months = {'03' : 1 , '04' : 2,'05' : 3 , '06' : 4 , '07' : 5 ,
		'08': 6 ,'09':7  , '10':8 , '11': 9 , '12': 10 , '01':11, "02":12}# dict with corresponding values as  in Zellers formula
		m = int(months[self.month])
		D = int(self.year[::-2])#slice the last 2 digits of the year
		C = int(self.year[:2])# get the first 2 digits of the year
		'''tells the day
		Zeller's Rule

The following formula is named Zeller's Rule after a Reverend Zeller.
[x] means the greatest integer that is smaller than or equal to x. 
You can find this number by just dropping everything after the decimal point. 
zFor example, [3.79] is 3. Here's the formula:

f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C.
k is the day of the month. Let's use January 29, 2064 as an example. For this date, k = 29.
m is the month number. Months have to be counted specially for Zeller's Rule: March is 1, April is 2, and so on to February, which is 12. (This makes the formula simpler, because on leap years February 29 is counted as the last day of the year.) Because of this rule, January and February are always counted as the 11th and 12th months of the previous year. In our example, m = 11.
D is the last two digits of the year. Because in our example we are using January (see previous bullet) D = 63 even though we are using a date from 2064.
C stands for century: it's the first two digits of the year. In our case, C = 20.
		'''
		f = int(self.date) + math.floor(((13*m)-1)/5) + D + math.floor(D/4) + math.floor(C/4) - 2*C
		'''
		Once we have found f, we divide it by 7 and take the remainder. Note that if the result for f is negative, 
		care must be taken in calculating the proper remainder. Suppose f = -17. When we divide by 7, we have to follow the same rules
		 as for the greatest integer function; namely we find the greatest multiple of 7 less than -17, so the remainder will be 
		 positive (or zero). -21 is the greatest multiple of 7 less than -17, so the remainder is 4 since -21 + 4 = -17. 
		 Alternatively, we can say that -7 goes into -17 twice, making -14 and leaving a remainder of -3,
		  then add 7 since the remainder is negative, so -3 + 7 is again a remainder of 4.'''
		f_1 = round(abs(int(f)%7))
		Days = {0 : "Sunday" , 1: "Monday" , 2: " Tuesday" , 3: "Wednesday" , 4:"Thursday" , 5: "Friday" , 6:" Saturday"}
		Day = Days[f_1]

		return f" {self.date}-{self.month}-{self.year} falls on {Day}"


d , m , y = input("Enter the date.(dd)\t") , input("Enter the month.(mm)\t") , input("Enter the year.(yyyy)\t")

user_req = Day(d , m , y)
print(user_req.tellDay())