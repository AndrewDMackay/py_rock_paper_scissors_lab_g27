from models.player import Player

class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play(self):
        if self.player_1.player_choice == self.player_2.player_choice:
            return(f"{self.player_1.player_name}, and {self.player_2.player_name} both selected {self.player_1.player_choice}.. It's a tie!")
        elif self.player_1.player_choice == "rock":
            if self.player_2.player_choice == "scissors":
                return(f"Rock crushes scissors! {self.player_1.player_name} wins! {self.player_2.player_name} loses!")
            else:
                return(f"Paper covers rock! {self.player_2.player_name} wins! {self.player_1.player_name} loses..")
        elif self.player_1.player_choice == "paper":
            if self.player_2.player_choice  == "rock":
                return(f"Paper covers rock! {self.player_1.player_name} wins! {self.player_2.player_name} loses..")
            else:
                return(f"Scissors cuts paper! {self.player_2.player_name} wins! {self.player_1.player_name} loses..")
        elif self.player_1.player_choice == "scissors":
            if self.player_2.player_choice == "paper":
                return(f"Scissors cuts paper! {self.player_1.player_name} wins! {self.player_2.player_name} loses..")
            else:
                return(f"Rock crushes scissors! {self.player_2.player_name} wins! {self.player_1.player_name} loses..")


