import random
def get_choices():

 player_choice = input("Enter a choice(rock,paper,scissors:")
 computer_choice = random.choice(options)
 options=["rock","paper","scissors"]
 #dictionaries in python are used to store data values in key value pairs
 choices={"player":player_choice,"computer":computer_choice}
 return choices

def check_win(player,computer):
    #f string is a simpler way to combine strings together
    print(f"You chose {player}, computer chose {computer}" )
    if player == computer:
     return "It's a tie!"
    elif player == "rock":
     if computer == "scissors":
         return "Rock smashes scissors! you win"
     else:
         return "Paper covers rock! you lose"
    elif player == "paper":
     if computer == "rock":
         return "Paper covers rocks! you win"
     else:
         return "scissors cuts paper! you lose"
    elif player == "scissors":
     if computer == "paper":
         return "scissors cuts paper! you win"
     else:
         return "Rock smashes scissors! you lose"

