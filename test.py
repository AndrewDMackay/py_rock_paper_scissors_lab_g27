import random

# User input, Rock, Paper, Scissors..

# Possible computer choices, Rock, Paper, Scissors..

# Randomise possible computer choices.. 

# Print statements for the user, and computer choices..

# While loop, to keep the game running, added player input at the end of the program..

# Print statements for tie, best placed first, eliminates the most possibilites..

# Print statements, if, elif, else, for differing results..

# Player input to choose whether to play again, repeating the program, or breaking the loop..

while True:
    player_choice = input("Enter your choice! [ Rock, paper, or scissors? ]: ")
    possible_choices = ["rock", "paper", "scissors"]
    opponent_choice = random.choice(possible_choices)
    print(f"You chose {player_choice}! Your opponent chose {opponent_choice}!")

    if player_choice == opponent_choice:
        print(f"You, and your opponent both selected {player_choice}.. It's a tie!")
    elif player_choice == "rock":
        if opponent_choice == "scissors":
            print("Rock crushes scissors! You win!")
        else:
            print("Paper covers rock! You lose..")
    elif player_choice == "paper":
        if opponent_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose..")
    elif player_choice == "scissors":
        if opponent_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock crushes scissors! You lose..")

    play_again = input("Play again.. [ Yes or No? ]: ")
    if play_again.lower() != "yes":
        break
