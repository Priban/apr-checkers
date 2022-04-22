
from graphics import Graphics
from rock import Rock
from queen import Queen


class Game():

    def __init__(self):
        self._board = [[None for j in range(8)] for i in range(8)]
        self.fill_in_figures()
        self._game_over = False
        self._highlighted = None

    def start(self):
        print("zadávej pozice ve formátu např. '1 3'")
        while not self._game_over:
            self.draw()
            self.update()

    def update(self):
        print("update")
        self.require_player_to_highlight_figure()
        self.draw()
        self.require_player_to_move()

    def require_player_to_move(self):
        while True:
            coords = input("táhni: ").split(" ")

            try:
                (x, y) = list(map(lambda c: int(c), coords))
            except ValueError:
                print("špatný formát souřadnic")
                continue

            if x > 8 or y > 8 or x < 1 or y < 1:
                print("souřadnice jsou od 1 do 8")
                continue

            try:
                self._highlighted.move(x - 1, y - 1, self._board)
                self._highlighted = None
                return
            except Exception as e:
                print("táhneš špatně táhni do prdele, důvod: " + str(e))

    def require_player_to_highlight_figure(self):
        while True:
            coords = input("označ figurku: ").split(" ")

            try:
                (x, y) = list(map(lambda c: int(c), coords))
            except ValueError:
                print("špatný formát souřadnic")
                continue

            if x > 8 or y > 8 or x < 1 or y < 1:
                print("souřadnice jsou od 1 do 8")
                continue

            if self._board[x - 1][y - 1] == None:
                print("na tomto políčku není žádná figurka")
                continue

            self._highlighted = self._board[x - 1][y - 1]
            return

    def draw(self):
        Graphics.draw(self._board, self._highlighted)

    def fill_in_figures(self):
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self._board[i][j] = Rock(0)

        for i in [5, 6, 7]:
            for j in range(8):
                if (i + j) % 2 == 0:
                    self._board[i][j] = Rock(1)
