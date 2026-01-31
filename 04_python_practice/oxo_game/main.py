from game import Game
import click
# pip install click
@click.command()
@click.option('--rounds', default=0, help='Number of rounds to play before auto-exit.')

def gameplay(rounds):
    name = input("Enter your name: ")        # Ask for player name
    game = Game(name)                         # Create a new game
    count = 1

    while True:
        if rounds > 0 and count > rounds:
            print("Thanks for playing!")
            break
        user_input = input(
            "Choose [rock, paper, scissors] or 'quit': ").strip().lower()
        if user_input == 'quit':
            print("Thanks for playing!")
            break
        game.set_player_choice(user_input)    # Set player move
        if game.player.choice:                # Only play if input was valid
            game.play_round()      
            count += 1                           # Play one round


if __name__ == "__main__":
    gameplay()