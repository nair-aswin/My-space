import random

target = random.randint(1, 100)   
# print(target)

print("================= Welcome to the Guess the Number Game! ================= " \
"\n I have selected a number between 1 and 100. " \
"Can you guess it? \n Let's get started!")

while True:
    userNum = int(input("Guess the number (1-100): "))
    if userNum == target:
        print("Congratulations! You guessed the number!")
        break # exit the loop
    elif userNum < target:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")

print("==================YOU WON==================")