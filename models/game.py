from models.player import Player

class Game:
    def __init__(self):
        pass

    # Write a game class that has a function that takes in the 2 players..
    # Compares their choices and returns the winning player. 
    # If it is a draw the player should be None type..

    player1 = Player("Steve", "rock")
    player2 = Player("Stan", "scissors")

    players = [player1, player2]

    def play_game(self):
        if self.player1.player_choice == self.player2.player_choice:
            return(f"{self.player1.player_name}, and {self.player2.player_name} both selected {self.player1.player_choice}.. It's a tie!")
        elif self.player1.player_choice == "rock":
            if self.player2.player_choice == "scissors":
                return(f"Rock crushes scissors! {self.player1.player_name} wins! {self.player2.player_name} loses!")
            else:
                return(f"Paper covers rock! {self.player2.player_name} wins! {self.player1.player_name} loses..")
        elif self.player1.player_choice == "paper":
            if self.player2.player_choice  == "rock":
                return(f"Paper covers rock! {self.player1.player_name} wins! {self.player1.player_name} loses..")
            else:
                return(f"Scissors cuts paper! {self.player2.player_name} wins! {self.player1.player_name} loses..")
        elif self.player1.player_choice == "scissors":
            if self.player2.player_choice == "paper":
                return(f"Scissors cuts paper! {self.player1.player_name} wins! {self.player1.player_name} loses..")
            else:
                return(f"Rock crushes scissors! {self.player2.player_name} wins! {self.player1.player_name} loses..")
