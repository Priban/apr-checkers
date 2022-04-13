from grid import Grid
from game import Game


grid = Grid(8)
grid.draw([
    {"location": (1, 1), "color": 0},
    {"location": (6, 0), "color": 1},
    {"location": (5, 4), "color": 0},
    {"location": (7, 7), "color": 1},
    {"location": (1, 7), "color": 0}
])

game = Game()
game.start()