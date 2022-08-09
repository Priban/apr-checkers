from anytree import Node

# tahy budou v poli které se vygeneruje při začátku kola hráče,
# vyfiltrují se ty, které nejsou platné (např. existuje jeden nebo více kde dochází k braní)

# tahy se budou generovat tak, že se vybere Node ze kterého se udělají children z cest o jeden stupeň dál
# a pak se u každého child udělá ten stejný proces (vzniklý strom může mít Node s největší hloubkou,
# který je pak jediným platným tahem)

class MoveLogic():

    def find_moves(self, figure, board):
        moves = Node(figure.get_position(board))