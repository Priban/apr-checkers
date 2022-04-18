from figure import Figure

class Queen(Figure):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self):
        pass

    def move_is_valid(self, x, y, board):
        return True