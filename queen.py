from figure import Figure

class Queen(Figure):

    def __init__(self, color):
        super().__init__(color)

    def move(self):
        pass

    def move_is_valid(self, x, y, board):
        return True