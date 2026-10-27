"""
Workflow of Project:
1- Input from user(Rock, Paper, Scissor)
2- Computer Choice( Computer Choose Will Randomly Not Conditionally)
3- Result Print


Cases:
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win 

B- Paper
Paper - Paper = Tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor Win

C- Scissor
Scissor - Scissor = Tie
Scissor - Paper = Scissor Win
Scissor - Rock = Rock Win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your Move (Rock, Paper, Scissor): ")
Comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, computer choice = {Comp_choice}")

if user_choice not in item_list:
    print("Invalid Move, Please Enter Rock, Paper, or Scissor.")

elif user_choice == Comp_choice:
    print("Both choose the same : Match Tie")

elif user_choice == "Rock":
    if Comp_choice == "Paper":
        print("Paper cover Rocks = Computer Win")
    else:
        print("Rock Smash Scissors = You Win")

elif user_choice == "Paper":
    if Comp_choice == "Rock":
        print("Paper Cover Rocks = You Win")
    else:
        print("Scissor Cut Paper = Computer Win")

elif user_choice == "Scissor":
    if Comp_choice == "Paper":
        print("Scissor cut Paper = You Win")
    else:
        print("Rock Smash Scissor = Compter Win")



