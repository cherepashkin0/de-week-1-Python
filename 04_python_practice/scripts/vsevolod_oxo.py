# import click
import random
from collections import defaultdict
import click

print('x-mark always starts')
class Game():
    WIN_POSES = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
           [0, 3, 6], [1, 4, 7], [2, 5, 8],
           [0, 4, 8], [2, 4, 6]]
    def __init__(self):
        self.field = ['_']*9
    def line_to_square(self):
        return "\n".join([str(self.field[3*i:3*i+3]) for i in range(len(self.field)//3)])
    def move(self, pos, mark):
        pos = int(pos)
        if self.field[pos] != '_':
            print('you cannot occupy cell if it is already occupied')
            raise RuntimeError
        self.field[pos] = mark
        diff = self.field.count('x') - self.field.count('o')
        print('diff = ', diff)
        if diff not in [0, 1]:
            print('you cannot make two moves for one turn')
            raise RuntimeError
        self.check_win()
        print(self.line_to_square())
    def how_many_moves_now(self):
        return f"{self.field.count('x')} x-marks and {self.field.count('o')} o-marks"
            # if mark == 'x':
            #     self.moves_counter_x += 1
            # else:
            #     self.moves_counter_o += 1
        # print(self.field.line_to_square())
    def check_win(self):
        for pos_triplet in self.WIN_POSES:
            dct = defaultdict(int)
            for pos in pos_triplet:
                dct[self.field[pos]] += 1
            if dct['x'] == 3:
                print('x-mark won')
                exit(1)
            elif dct['o'] == 3:
                print('o-mark won')
                exit(1)
    def get_unocuppied_pos(self):
        return [i for i, x in enumerate(self.field) if x == "_"]
        

game = Game()
while True:
    user_move_read = input(f"Enter a number from a list {game.get_unocuppied_pos()}")
    game.move(user_move_read, 'x')

game = Field((3, 3))
print(game.move(0, 'x'))
print(game.how_many_moves_now())
print(game.move(4, 'o'))
print(game.how_many_moves_now())
print(game.move(3, 'x'))
print(game.how_many_moves_now())
print(game.move(5, 'o'))
print(game.how_many_moves_now())
print(game.move(6, 'x'))

# TODO:
# 1. if user does illegal move, return him to previous state
# 2. 


        