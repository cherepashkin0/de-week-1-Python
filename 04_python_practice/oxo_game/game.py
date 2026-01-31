import random
from decorators import log_game, validate_choice
from player import Player


class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.computer = Player("Computer")

    @validate_choice
    def set_player_choice(self, choice):
        self.player.set_choice(choice)

    def generate_computer_choice(self):
        choice = random.choice(['rock', 'paper', 'scissors'])
        self.computer.set_choice(choice)

    @log_game
    def play_round(self):
        self.generate_computer_choice()  # Get computer's move
        print(self.player)              # Show both choices
        print(self.computer)
        self.determine_winner()         # Decide winner

    def determine_winner(self):
        p = self.player.choice
        c = self.computer.choice

        if p == c:
            print("It's a tie!")
        elif (p == 'rock' and c == 'scissors') or \
             (p == 'scissors' and c == 'paper') or \
             (p == 'paper' and c == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")