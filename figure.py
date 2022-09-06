from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, color):
        self._color = color
    
    # kdokoliv TODO: odstranění přeskočených figur
    def move(self, x, y, board):
        (previous_x, previous_y) = self.get_position(board)
        board[previous_x][previous_y] = None
        board[x][y] = self
        print("ahoj")

    @abstractmethod
    def move_is_valid(self, position, current_position, board):
        return

    def get_position(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == self: return (i, j)

    def get_color(self):
        return self._color

        
