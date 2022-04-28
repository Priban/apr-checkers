
from graphics import Graphics
from rock import Rock
from queen import Queen
import csv
from file_loader import FileLoader

class Game():


    def __init__(self):
        self._fl = FileLoader("csv_file.csv")
        self._board = [[None for j in range(8)] for i in range(8)]
        self.fill_in_figures()
        self._game_over = False
        self._highlighted = None

    def start(self):
        print("zadávej pozice ve formátu např. 'a 3'")
        while not self._game_over:
            self.draw()
            self.update()

    def update(self):
        print("update")

        #csv_file přepíše nové pozice figur v souboru

        self.require_player_to_highlight_figure()
        self.draw()
        self.require_player_to_move()
        self._fl.save_game(self._board)

    def require_player_to_move(self):
        columns = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7,"h": 8}
        while True:
            coords = input("táhni: ").split(" ") 

            if coords[0] not in columns:
                print("souřadnice jsou od a do h")
                continue

            coords[0] = columns[coords[0]]
            coords = coords[::-1]

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
        columns = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7,"h": 8}
        while True:
            coords = input("vyber si figurku: ").split(" ") 

            if coords[0] not in columns:
                print("souřadnice jsou od a do h")
                continue

            coords[0] = columns[coords[0]]
            coords = coords[::-1]

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
        for position in self._fl.load_game():
                self._board[position[0]][position[1]] = Rock(position[2])