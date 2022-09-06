from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, color):
        self._color = color
    
    def move(self, x, y, board):
        (previous_x, previous_y) = self.get_position(board)
        board[previous_x][previous_y] = None
        board[x][y] = self
        self.delete_jumped_figures(x, y, previous_x, previous_y, board)

    @abstractmethod
    def move_is_valid(self, position, current_position, board):
        return

    def get_position(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == self: return (i, j)

    def get_color(self):
        return self._color

    # projedeme diagonálu tahu a smažeme figurku, která na ní byla
    def delete_jumped_figures(self, x, y, previous_x, previous_y, board):
        (dir_x, dir_y) = (int((x-previous_x)/abs(x-previous_x)), int((y-previous_y)/abs(y-previous_y)))
        position_x = previous_x + dir_x
        position_y = previous_y + dir_y
        while position_x != x:
            if board[position_x][position_y]:
                board[position_x][position_y] = None
            position_x += dir_x
            position_y += dir_y