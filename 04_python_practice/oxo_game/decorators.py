def log_game(func):
    def wrapper(*args, **kwargs):
        print("Starting a new round!")
        result = func(*args, **kwargs)
        print("Round ended.\n")
        return result
    return wrapper


def validate_choice(func):
    def wrapper(self, choice):
        valid_choices = ['rock', 'paper', 'scissors']
        if choice.lower() not in valid_choices:
            print(
                f"Invalid choice: '{choice}'! Choose rock, paper, or scissors.")
            self.player.choice = None  # Reset choice so the game won't play
            return None
        return func(self, choice)
    return wrapper