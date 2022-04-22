from figure import Figure


class Rock(Figure):

    def __init__(self, color):
        super().__init__(color)

    def move_is_valid(self, x, y, board):
        (current_x, current_y) = self.get_position(board)
        # když (i + j) % 2 == 0
        if not (x + y) % 2 == 0: raise Exception("Táhni jenom na bílý políčka")

        # u kamene o jeden řádek, u královny jakýkoliv
        if self._color:
            if not x <= current_x: raise Exception("Musíš nahoru")
        else:
            if not x >= current_x: raise Exception("Musíš dolu")

        # když na poli není figurka
        if board[x][y] != None: raise Exception("Tady už někdo je")

        # když není jiný tah na kterém by se skákalo

        return True

    def promote_to_queen(self):
        pass
