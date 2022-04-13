from grid import Grid
<<<<<<< HEAD
from game import Game

=======
from figure import Figure
from rock import Rock
from queen import Queen

rock_1 = Rock(6, 0, 0)
rock_2 = Rock(1, 1, 1)
>>>>>>> 814d08966afc37ba858ba403ef6bd8d8803e3300

grid = Grid(8)
grid.draw([
    {rock_1.give_information()}
])

game = Game()
game.start()