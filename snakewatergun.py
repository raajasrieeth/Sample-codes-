import random

print("Game started")
option_list = ["Snake", "Water", "Gun"]
print("Type S for selecting Snake;W for water and G for gun")
user_score = 0
comp_score = 0
chancenum = 10
while chancenum >= 1:
    comp_pick = random.choice(option_list)
    user_pick = input().capitalize()
    if user_pick == "S":
        chancenum = chancenum - 1
        if comp_pick == "Snake":
            print("computer chose", comp_pick, "so, draw")
            continue
        elif comp_pick == "Water":
            print("computer chose", comp_pick, "so, You Win!!")
            user_score=user_score+1
            continue
        else:
            print("computer chose", comp_pick, "so, You Lose!!")
            comp_score=comp_score+1
            continue
    elif user_pick == "W":
        chancenum = chancenum - 1
        if comp_pick == "Snake":
            print("computer chose", comp_pick, "so, You Lose!")
            comp_score=comp_score+1
            continue
        elif comp_pick == "Water":
            print("computer chose", comp_pick, "so, draw!")
            continue
        else:
            print("computer chose", comp_pick, "so, You Win!!")
            user_score=user_score+1
            continue
    else:
        chancenum = chancenum - 1
        if comp_pick == "Snake":
            print("computer chose", comp_pick, "so, You Win!!")
            user_score=user_score+1
            continue
        elif comp_pick == "Water":
            print("computer chose", comp_pick, "so, You Lose!!")
            comp_score=comp_score+1

            continue
        else:
            print("computer chose", comp_pick, "so, draw!!")
            continue
print("Game Ended")
print("Scores are as follows:\n", "Computer:", comp_score, "\n" "You:", user_score, "\n")
if user_score > comp_score:
    print("You win!!!")
elif user_score < comp_score:
    print("You lost!!")
else:
    print("It was a draw")


