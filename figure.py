from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, color):
        self._color = color
    
    def move(self, x, y, board):
        if self.move_is_valid(x, y, board):
            (previous_x, previous_y) = self.get_position(board)
            board[previous_x][previous_y] = None
            board[x][y] = self
            print("ahoj")

    @abstractmethod
    def move_is_valid(self, x, y, board):
        return

    def get_position(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == self: return (i, j)

        
