from grid import Grid
from game import Game
from figure import Figure
from rock import Rock
from queen import Queen

rock_1 = Rock(6, 0, 0)
rock_2 = Rock(1, 1, 1)

print(rock_1.get_information())


grid = Grid(8)
grid.draw([
    {"location": (1, 1), "color": 0},
    {"location": (6, 0), "color": 1},
    {"location": (5, 4), "color": 0},
    {"location": (7, 7), "color": 1},
    {"location": (1, 7), "color": 0},
    rock_1.get_information()
])

game = Game()
game.start()