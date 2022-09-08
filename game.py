from graphics import Graphics
from move_logic import MoveLogic
from rock import Rock
from queen import Queen
import csv
from file_loader import FileLoader
from anytree import Node, RenderTree, ContStyle, findall, find

class Game():

    def __init__(self):
        self._fl = FileLoader("csv_file.csv")
        self._ml = MoveLogic()
        self._game_over = False
        self._highlighted = None
        self._player_on_turn = 0
        self._current_possible_moves = []

    def start(self):
        self._board = self.init_board()
        self._current_possible_moves = self._ml.find_all_possible_moves(self._board, player_on_turn=self._player_on_turn)
        print("zadávej pozice ve formátu např. 'a3'")
        while not self._game_over:
            self.draw()
            self.update()

        print("Vyhrál hráč s " + ("křížky" if self._player_on_turn == 0 else "kolečky"))

    def update(self):
        if self._player_on_turn == 0:
            print("Na řadě je hráč s kolečky")
        else:
            print("Na řadě je hráč s křížky")

        self.require_player_to_highlight_figure()
                
        # pro debug
        print("----------------- Aktuální možné tahy -----------------")
        for move in self._current_possible_moves:
            print(RenderTree(move, style=ContStyle()))
        print("-------------------------------------------------------")

        self.draw()
        self.require_player_to_move()

        if self._player_on_turn == 0:
            self._player_on_turn = 1
        else:
            self._player_on_turn = 0

        self._current_possible_moves = self._ml.find_all_possible_moves(self._board, player_on_turn=self._player_on_turn)

        if len(self._current_possible_moves) == 0:
            self._game_over = True
            return

        self._fl.save_game(self._board)


    def require_player_to_move(self):
        columns = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7,"h": 8}

        # Tady zjistíme, jaký strom používáme
        current_move = None
        for move in self._current_possible_moves:
            if move.position == self._highlighted.get_position(self._board):
                current_move = move
                
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
            
            # pokud nalezne move s pozicí highlighted figury
            position_to_move = find(current_move, lambda node: node.position == (x-1, y-1), maxlevel=2)
            if position_to_move:
                self._highlighted.move(x - 1, y - 1, self._board)
                # pokud po tahu následuje další tah
                if not position_to_move.is_leaf:
                    current_move = position_to_move # useknutí předchozího tahu ze stromu
                    self.draw()
                    continue      
                else:
                    self._highlighted = None
                    return


            print("Sem táhnout nemůžeš, táhni znova.")

            # tady se vybere Node ze spojového stromu který je potomkem pozice highlighted figury
            # a bude obsahovat buďto validní tah nebo zprávu proč je tah špatný,
            # pokud Node ve stromu neexistuje je tah mimo dosah

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

            for move in self._current_possible_moves:
                if move.position == (x-1, y-1):
                    self._highlighted = self._board[x - 1][y - 1]
                    return

            print("S touhle figurkou se nedá táhnout.")


    def draw(self):
        Graphics.draw(self._board, self._highlighted, list(map(lambda node: node.position, self._current_possible_moves)))
    
    def init_board(self):
        while True:
            load_from_csv = input("0 -> začít novou hru | 1 -> načíst rozehranou hru: ")
            if load_from_csv == "0" or load_from_csv == "1":
                break

        if load_from_csv == "1":
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
            figure = None
            if position[2] == 0:
                figure = Rock(0)
            elif position[2] == 1:
                figure = Queen(0)
            elif position[2] == 2:
                figure = Rock(1)
            else:
                figure = Queen(1)
            board[position[0]][position[1]] = figure
        return board

    def load_default_board(self):
        board = [[None for j in range(8)] for i in range(8)]
        for i in [0, 1, 2, 5, 6, 7]:
            for j in range(4):
                board[i][j * 2 + i % 2] = Rock(0 if i < 3 else 1)
        return board