from turtle import position
from anytree import Node
from rock import Rock

# tahy budou v poli které se vygeneruje při začátku kola hráče,
# vyfiltrují se ty, které nejsou platné (např. existuje jeden nebo více kde dochází k braní)

# tahy se budou generovat tak, že se vybere Node ze kterého se udělají children z cest o jeden stupeň dál
# a pak se u každého child udělá ten stejný proces (vzniklý strom může mít Node s největší hloubkou,
# který je pak jediným platným tahem)

class MoveLogic():

    def find_moves(self, board, figure):
        moves = Node(figure.get_position(board), position=figure.get_position(board))
        starting_position = figure.get_position(board)

        # tady se v cyklu vyzkouší každá možná pozice a přidá se do stromu moves buď jako validní tah
        # nebo jako nevalidní tah se zprávou proč nelze provést
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                # pokud na cílovém poli stojí figura, zkusí se pole za ní (znovu +dx +dy)
                try:
                    if figure.move_is_valid((starting_position[0] + 1, starting_position[1] + 1), board):
                        move = Node((starting_position[0] + 1, starting_position[1] + 1), parent=moves, position=(starting_position[0] + 1, starting_position[1] + 1))
                except Exception as e:
                        move = Node()
        print(moves.children)

    def find_possible_moves(self, board, player_on_turn):
        figures_on_turn = self.find_figures_on_turn(board, player_on_turn)
        # for figure in figures_on_turn:
        #     print(figure.get_position(board))
        self.find_moves(board, figures_on_turn[8])

    def find_figures_on_turn(self, board, player_on_turn):
        figures = []
        for i in range(8):
            for j in range(8):
                if board[i][j] and board[i][j].get_color() == player_on_turn:
                    figures.append(board[i][j])
        return figures
