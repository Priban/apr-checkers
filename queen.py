from figure import Figure

class Queen(Figure):

    def __init__(self, color):
        super().__init__(color)

    def move(self):
        pass

    def move_is_valid(self, x, y, board):
        (currect_x, current_y) = self.get_position(board)
        
        if not (x + y) % 2 == 0: raise Exception("Táhni jenom na bílý políčka")

        if board[x][y] != None: raise Exception ("Tady už někdo je")

        return True