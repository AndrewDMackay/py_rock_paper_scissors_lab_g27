import random

# User input, Rock, Paper, Scissors..

user_action = input("Enter Your Choice! [ Rock, Paper, Scissors ]:")

# Possible computer actions, Rock, Paper, Scissors..

possible_actions = ["rock", "paper", "scissors"]

# Randomise possible computer actions.. 

computer_action = random.choice(possible_actions)

# Print statements for the user, and computer actions..

print(f"You chose {user_action}! Computer chose {computer_action}!")

