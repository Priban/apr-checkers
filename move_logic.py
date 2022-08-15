from anytree import Node, RenderTree, ContStyle
from rock import Rock

# tahy budou v poli které se vygeneruje při začátku kola hráče,
# vyfiltrují se ty, které nejsou platné (např. existuje jeden nebo více kde dochází k braní)

# tahy se budou generovat tak, že se vybere Node ze kterého se udělají children z cest o jeden stupeň dál
# a pak se u každého child udělá ten stejný proces (vzniklý strom může mít Node s největší hloubkou,
# který je pak jediným platným tahem)

class MoveLogic():
    
    # rekurzivně vygeneruje strom možných tahů
    def find_moves(self, board, figure, position=None, parent=None):
        position = figure.get_position(board) if not position else position
        moves = Node(position, position=position, valid=1, parent=parent)

        if isinstance(figure, Rock) and moves.depth == 1: return moves

        # tady se v cyklu vyzkouší každá možná pozice a přidá se do stromu moves buď jako validní tah
        # nebo jako nevalidní tah se zprávou proč nelze provést
        # pokud už není žádný potomek obsahující validní tah, uzavře se rekurze

        # pokud je depth > 0 
        for dx in [-1, 1]:
            dxpos = position[0] + dx
            if not (0 <= dxpos < 8): continue
            for dy in [-1, 1]:
                dypos = position[1] + dy
                if not (0 <= dypos < 8): continue
                dpos = (dxpos, dypos) 

                # pokud na cílovém poli stojí figura, zkusí se pole za ní (znovu +dx +dy)
                try:
                    if figure.move_is_valid(dpos, board, current_position=position):
                        move = self.find_moves(board, figure, dpos, moves)
                except Exception as e:
                    move = Node(dpos, parent=moves, position=dpos, valid=0, message=str(e))

        return moves

    def find_possible_moves(self, board, player_on_turn):
        figures_on_turn = self.find_figures_on_turn(board, player_on_turn)
        # for figure in figures_on_turn:
        #     print(figure.get_position(board))
        tree = self.find_moves(board, figures_on_turn[8])
        print(RenderTree(tree, style=ContStyle()))

    def find_figures_on_turn(self, board, player_on_turn):
        figures = []
        for i in range(8):
            for j in range(8):
                if board[i][j] and board[i][j].get_color() == player_on_turn:
                    figures.append(board[i][j])
        return figures
