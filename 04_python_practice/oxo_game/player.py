class Player:
    def __init__(self, name):
        self.name = name         # Each player has a name
        self.choice = None       # Choice is initially None

    def set_choice(self, choice):
        self.choice = choice.lower()  # Convert input to lowercase

    def __str__(self):
        # Nice print format
        return f"{self.name} chose {self.choice.capitalize()}"