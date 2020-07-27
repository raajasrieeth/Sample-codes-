import time
import PIL
print("Welcome to my first game")
health = 100

start=time.time()
class Choice():
	co = False
	ct = False
	def __init__(self , winningArg , losingArg , user_opt):
		self.winningArg = winningArg
		self.losingArg = losingArg
		self.user_opt = user_opt
	def winOrLose(self):
		if self.user_opt != self.winningArg and self.user_opt != self.losingArg:
			print("Enter a valid value!")

		elif self.user_opt == self.winningArg:
			self.ok = True
		else:
			self.ok = False





	# def option_choice(winningArg  , losingArg , user_opt):
	# 	if user_opt.lower() != winningArg and user_opt.lower() != losingArg:
	# 		print("Enter a proper value!!")
	# 	elif user_opt.lower() == winningArg:
	# 		return True
	# 	elif user_opt.lower() == losingArg:
	# 		return False
	def func_ch1(self):
		if self.ok == True:
			self.co = True
			print(f"You have chosen to go left and you are now near a river and have {health} health ")
		    
		else :
			self.co = False
			print("You fall and die!")
			pass
			
	def func_ch2(self):
		if self.co == True and self.ok == True :
			print(f"You went around the river and have {health} health left")
			self.ct =  True
		elif self.co == True and self.ok == False :
			health-=50
			print("You reached the bank , but on the way , you were bit by some fish and have ",health," health left")
			self.ct = False
		else:
			pass

	def func_ch3(self):
		# if self.co == False:
		# 	pass

		if self.ct  == True and self.ok  == True:
			print("You now have been teleported to another place.")
			time.sleep(1)
			print("But why?")
			time.sleep(1)
			print("Seems like you touched the mysterious handle")
			time.sleep(1)
			print("Anyways , you are still on the Earth")
			time.sleep(2)
			print("\n To continue")
		elif self.ct == False and self.ok == True:
			print("You now have been teleported to another place.")
			time.sleep(1)
			print("But why?")
			time.sleep(1)
			print("Seems like you touched the mysterious handle")
			time.sleep(1)
			print("Anyways , you are still on the Earth")
			time.sleep(2)
			print("\n To continue")
		elif self.ok == False:
			print("You drown in the lake and lose!")
		

try:
	name = input("Enter your name")
	age  = int(input("Enter your Age"))
	if age <5 or age >100:
		print("You are not eligible to play")
	else:
		game_entry= input(f"Hello, {name}. In this game, you have to make decisions.Do you want to play it? (yes/no)")

		if game_entry.lower() != "yes" and game_entry.lower() != 'no':
			print('Enter a valid value!!')
		elif game_entry.lower() == 'yes':
			c1=input("You are in a forest. Where to you want to go?(right/left)")
			ev = Choice("left" , "right"  , c1)
			ev.winOrLose()
			ev.func_ch1()
			c2 = input("Do you want to go across the river or around it?(across/around)")
			b = Choice("around" , "across"  , c2)
			b.winOrLose()
			b.func_ch2()
			c3=input("You now see a house and a lake. Where do you want to go?(house/lake)")
			c = Choice("house" , "lake"  , c3)
			c.winOrLose()
			c.func_ch3()
			
					
						
		else:
			print("OK , Thank you")
except ValueError :
	print("Age is a number!!")
finally :
	time.sleep(2)
	creds={"Developer":"Raaj Asrieeth MR" , "Plotting":"Raaj Asrieeth MR"}
	print("Thank You for playing!!")
	end = time.time()
	print('You took',int(end-start) ,'seconds to finish\n\n')
	print("Credits:")
	for key,value in creds.items():
		print(f"{key} is {value}")
