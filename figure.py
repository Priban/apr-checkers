from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    
    def move(self, x, y, board):
        if self.move_is_valid(x, y):
            board[x][y] = self

    @abstractmethod
    def move_is_valid(self, x, y, board):
        return

    def get_information(self):
        return {
            "location": (self.location_x, self.location_y),
            "color": self.color
        }
