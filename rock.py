from figure import Figure

class Rock(Figure):

    def __init__(self, color):
        super().__init__(color)

    def move_is_valid(self, position, board, current_position=None):
        (x, y) = position
        (current_x, current_y) = current_position if current_position else self.get_position(board)
        
        # když (i + j) % 2 == 0
        if not (x + y) % 2 == 0: return "Táhni jenom na bílý políčka"

        #print(x, y, current_x, current_y)
        # pokud je vzálenost <= 2
        if abs(x - current_x) > 2 or abs(y - current_y) > 2 or x - current_x == 0 or y - current_y == 0: return "Mimo dosah"

        if self._color:
            if not x < current_x: return "Musíš táhnout nahoru"
        else:
            if not x > current_x: return "Musíš táhnout dolu"

        # když na poli není figurka
        if board[x][y] != None: return "Na poli už se nachází figura" 
        
        # vrací 2 pro rozpoznání možnosti skákání
        #print("skakani")
        #print(abs(x - current_x), abs(y - current_y))
        if abs(x - current_x) == 2 and abs(y - current_y) == 2:
            jumped_figure = board[x - ((x - current_x) // abs(x - current_x))][y - ((y - current_y) // abs(y - current_y))]
            if jumped_figure and jumped_figure._color != self._color: 
                return 2
            else:
                return "Mimo dosah"

        return 1

    def promote_to_queen(self):
        pass