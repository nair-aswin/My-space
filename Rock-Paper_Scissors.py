import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors:").lower()
print("Computer chose:", computer)

if user == computer:
    print("It's a Tie!")

elif user == "rock":
    if computer == "scissors":
        print("You Win!")
    else:
        print("Computer wins!")

elif user == "paper":
    if computer == "rock":
        print("You Win!")
    else:
        print("Computer wins!")

elif user == "scissors":
    if computer == "paper":
        print("You Win!")
    else:
        print("Computer wins!")

else:
    print("Invalid input! Please choose either rock, paper or scissors.")
