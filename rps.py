import random

#Define variables
options = ['Rock', 'Paper', 'Scissors']
name = input("Enter your name:\n")
computerScore = 0
playerScore = 0
roundNumber = 0

print(f'Welcome {name.title()}!')

#Game
while roundNumber <= 3:
    computer_choice = random.choice(options)
    #title capitalizes user input
    player_choice = input("Enter Rock/Paper/Scissors:\n").title()
    print(f'Computer\'s choice: {computer_choice}')
    print(f'Your choice: {player_choice}')
    #roundNumber = roundNumber + 1
    roundNumber += 1
    if computer_choice == player_choice:
        print("This is a tie!")
    elif (computer_choice == "Rock" and player_choice == "Paper") or (computer_choice == "Paper" and player_choice == "Scissors") or (computer_choice == "Scissors" and player_choice == "Rock"):
        print("Congratulations, you win!")
        playerScore += 1
    elif (player_choice != "Rock") or (player_choice != "Scissors"):
        print("Invalid.")
    elif player_choice != "Paper":
        print("Invalid")
    else:
        print("Computer wins! Try again.")
        computerScore += 1
    print("-" * 29)
    print(f'|{"Number of Rounds:":18} {roundNumber:<8}|')
    print(f'|{"Score Board":-^27}|')
    print(f'|{name.title():<5} {"Score:":<9} {playerScore:<11}|')
    print(f'|{"Computer Score:":18} {computerScore:<8}|')
    print("-" * 30)
    print("")

#Game Over
if playerScore == computerScore:
    print("Draw! Nice try.")
elif playerScore < computerScore:
    print("Computer wins! Better luck next time")
else:
    print(f'{name.title()} wins! Nice game.')

#Try again - User enters Yes or No to Play again or Game over
