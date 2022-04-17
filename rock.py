from figure import Figure


class Rock(Figure):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move_is_valid(self, x, y, board):
        return True

    def promote_to_queen(self):
        pass
