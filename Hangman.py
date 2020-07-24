import random
import PIL
import webbrowser
import time



print("Welcome to Hangman")
print("You have to guess the word :")

# webbrowser.open("www.youtube.com")

words = ["World" , "Happy" ,"Healthy" , "Apple"  , ]
pick   = random.choice(words)
select_word = pick

def make_question_easy(pick = pick):

	for i in range(0, len(pick)//2):
		
		ques = pick.replace(pick[random.randint(0,len(pick)-1)] ,str(i) )
		pick  = ques
		i += 1

		return pick


def response():
	pass
	user_choice_pos = str(input("Enter the number(index) of the letter\t"))
	user_choice_let = str(input("Enter the letter for the number\t"))

	print(f"The real word is: {select_word.capitalize()}")


if __name__ == '__main__':
	print(__name__)
	print(make_question_easy())
	response()
