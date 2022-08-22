from anytree import Node, RenderTree, ContStyle, findall
from rock import Rock

# tahy budou v poli které se vygeneruje při začátku kola hráče,
# vyfiltrují se ty, které nejsou platné (např. existuje jeden nebo více kde dochází k braní)

# tahy se budou generovat tak, že se vybere Node ze kterého se udělají children z cest o jeden stupeň dál
# a pak se u každého child udělá ten stejný proces (vzniklý strom může mít Node s největší hloubkou,
# který je pak jediným platným tahem)

class MoveLogic():
    
    # rekurzivně vygeneruje strom možných tahů
    def find_moves_of_figure(self, board, figure, position=None, parent=None, jump=False):
        position = figure.get_position(board) if not position else position
        moves = Node(position, position=position, parent=parent, jump=jump)

        # tady se v cyklu vyzkouší každá možná pozice a pokud na ni lze táhnout, přidá se do stromu moves jako validní tah
        # pokud už není žádný potomek obsahující validní tah, uzavře se rekurze

        # udělat že se vyzkouší všechna prázdná pole
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] != None: continue
                pos = (i, j) 
                
                validation = figure.move_is_valid(pos, board, current_position=position)
                if validation == 1: # pokud posuzovaný tah je normálním tahem
                    move = Node(pos, parent=moves, position=pos, jump=False)
                elif validation == 2: # pokud posuzovaný tah je skokem, pokračuje rekurze dál
                    move = self.find_moves_of_figure(board, figure, pos, moves, True)
                else: # nevalidní tah
                    ...
                    # move = Node(pos, parent=moves, position=pos, valid=0, message=validation)

        return moves

    def find_all_possible_moves(self, board, player_on_turn):
        figures_on_turn = self.find_figures_on_turn(board, player_on_turn)
        all_moves = [self.find_moves_of_figure(board, figure) for figure in figures_on_turn]

        # vyfiltrování tahů s délkou 0
        all_moves = [move for move in all_moves if move.height > 0]

        # pokud existují tahy kde se skáče, ostatní se odstraní
        # TODO přednost skákání dámy
        jump_moves = [move for move in all_moves if findall(move, lambda node: node.jump == True)]

        if len(jump_moves) > 0: 
            all_moves = jump_moves

        return all_moves
        
    def find_figures_on_turn(self, board, player_on_turn):
        figures = []
        for i in range(8):
            for j in range(8):
                if board[i][j] and board[i][j].get_color() == player_on_turn:
                    figures.append(board[i][j])
        return figures