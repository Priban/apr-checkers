
from graphics import Graphics
from rock import Rock

class Game():

    def __init__(self):
        self._grid = [[None for j in range(8)] for i in range(8)]
        self.fill_in_figures()
        self._game_over = False

    def start(self):
        while not self._game_over:
            self.update()
            self.draw()
            
    def update(self):
        print("update")
        input("teď hráč zadá pohyb: ")
           
    def draw(self):
        Graphics.draw(self._grid)

    def fill_in_figures(self):
      for i in range(3):
        for j in range(8):
          if (i + j) % 2 == 0:
            self._grid[i][j] = Rock(i, j, 0)

      for i in [5, 6, 7]:
        for j in range(8):
          if (i + j) % 2 == 0:
            self._grid[i][j] = Rock(i, j, 1)