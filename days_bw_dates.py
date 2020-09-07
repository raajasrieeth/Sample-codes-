from datetime import date 
import datetime

def numberOfDays(date1, date2):
	'''format:yyyy , mm , dd'''
	return (date2-date1).days 

today  = datetime.datetime.today()
# y , m , d = int
date1 = date(2006 , 2 , 6)

date2 = date(int(today.year) , int(today.month) , int(today.day))

print(numberOfDays(date1,  date2) ," Days have elapsed since",date1 )

#seconds:
def secondsOld(*args):
	d = [[2006, 2 , 6],[int(today.year) , int(today.month) , int(today.day)]]
	for input in args:
		i = 0
		d.replace(input , i)
		i+= 1

	date1 = date(d[0][0] , d[0][1] , d[0][2])#my birthday
	date2 = date(d[1][0] , d[1][1] , d[1][2])#today
	return ((date2-date1).days)*23*3600+ (56*60)#seconds in a day ,  with 23hrs and 56 min.
print(secondsOld(),"Seconds have elapsed since the date ",date1, "(rough estimate) ")