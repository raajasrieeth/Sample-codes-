import random
import PIL
import webbrowser
import time
from functools import lru_cache


print("Welcome to Hangman")
print("You have to guess the word :")

# webbrowser.open("www.youtube.com")

words = ["World" , "Happy" ,"Healthy" , "Apple"  , ]
pick   = random.choice(words)
select_word = pick
@lru_cache(maxsize=1)

def make_question_easy(pick = pick):

	for i in range(0, len(pick)//2):
		l = pick[random.randint(0,len(pick)-1)]
		ques = pick.replace(l ,str(i) )#changes 1 letter , of a random 
		# position , given by the random generator.
		# and the position of the letter is taken by the currently 
		# iterating number. 
		pick  = ques # assigns the new value


	return pick


def response(pick = pick):

	for x in range(len(pick)//2):
		user_choice_pos = str(input("Enter the number(index) of the letter\t"))
		user_choice_let = str(input("Enter the letter for the number\t"))

if __name__ == '__main__':
	print(make_question_easy())
	response()
