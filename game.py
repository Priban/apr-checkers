from graphics import Graphics
from rock import Rock
from queen import Queen
import csv
from file_loader import FileLoader

class Game():

    def __init__(self):
        self._fl = FileLoader("csv_file.csv")
        self._game_over = False
        self._highlighted = None
        self._turn_of_player = 0

    def start(self):
        self._board = self.init_board()
        print("zadávej pozice ve formátu např. 'a 3'")
        while not self._game_over:
            self.draw()
            self.update()

    def update(self):
        self.require_player_to_highlight_figure()
        self.draw()
        self.require_player_to_move()
        self._fl.save_game(self._board)

    def require_player_to_move(self):
        columns = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7,"h": 8}
        while True:
            coords = list(input("táhni: "))

            if coords[0] not in columns:
                print("souřadnice jsou od a do h")
                continue

            coords[0] = columns[coords[0]]
            coords = coords[::-1]

            # zkusí coords převést na int
            try:
                (x, y) = list(map(lambda c: int(c), coords))
            except ValueError:
                print("špatný formát souřadnic")
                continue

            if x > 8 or y > 8 or x < 1 or y < 1:
                print("souřadnice jsou od 1 do 8")
                continue

            try:
                # tady se vybere Node ze spojového stromu který má root pozici highlighted figury
                # a bude obsahovat buďto validní tah nebo zprávu proč je tah špatný,
                # pokud Node ve stromu neexistuje je tah mimo dosah
                self._highlighted.move(x - 1, y - 1, self._board)
                self._highlighted = None
                return
            except Exception as e:
                print("táhneš špatně táhni do prdele, důvod: " + str(e))

    def require_player_to_highlight_figure(self):
        columns = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7,"h": 8}
        while True:
            coords = list(input("vyber si figurku: "))

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

    def init_board(self):
        while False: # sem potom True
            load_from_csv = input("0 -> začít novou hru | 1 -> načíst rozehranou hru: ")
            if load_from_csv == "0" or load_from_csv == "1":
                break

        load_from_csv = False

        if load_from_csv == "1": # pro debug se vždy načte default board
            try:
                return self.load_board_from_csv()
            except FileNotFoundError:
                print("Soubor nenalezen :(")
                return self.load_default_board()
        else:
            return self.load_default_board()

    def load_board_from_csv(self):
        board = [[None for j in range(8)] for i in range(8)]
        for position in self._fl.load_game():
                board[position[0]][position[1]] = Rock(position[2])
        return board

    def load_default_board(self):
        board = [[None for j in range(8)] for i in range(8)]
        for i in [0, 1, 2, 5, 6, 7]:
            for j in range(4):
                board[i][j * 2 + i % 2] = Rock(0 if i < 3 else 1)
        return board