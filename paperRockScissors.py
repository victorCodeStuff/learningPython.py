import random

userInput = input("What will you play? ") 

computerChoice = random.randint(1,3)
if computerChoice == 1:
    computerChoice = "scissors"
elif computerChoice == 2:
    computerChoice = "paper"
elif computerChoice == 3:
    computerChoice = "rock"
 
print("Computer choose:", computerChoice)

if computerChoice == userInput:
    print('Its a tie')
elif computerChoice == 'rock' and userInput == 'paper':
    print('You won')
elif computerChoice == 'paper' and userInput == 'scissors':
    print('you won')
elif computerChoice == "scissors" and userInput == "rock":
    print('You won')

elif computerChoice == 'paper' and userInput == 'rock':
    print('You lost')
elif computerChoice == 'scissors' and userInput == 'paper' :
    print('you lost')
elif computerChoice == "rock" and userInput == "scissors":
    print('You lost')

