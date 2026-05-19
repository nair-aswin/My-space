import random


print("-"*50)
print("WELCOME TO GUESS THE NUMBER!")
print("RULES: Guess the number and Win \n       Enter a number between 1 and 100\n       Enter Whole numbers only")
print("-"*50)

secret_number = random.randint(1,100)
attempts = 0


while True:
     try:
         guess = int(input("Enter the number: "))
     except ValueError:
        print("Enter a Valid Entry, Please try again")
        continue

     attempts += 1
     if secret_number == guess:
        print("You have guessed the correct number!")
        print("Congratualtions you won!")
        print(f"you have completed the game in {attempts} Attempts")
        break
     elif secret_number < guess:
         print("Too High, Guess lower")
     elif secret_number > guess:
         print("Too low, Guess Higher!")


