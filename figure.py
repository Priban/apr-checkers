from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, location_x, location_y, color):
        self.location_x = location_x
        self.location_y = location_y
        self.color = color

    @abstractmethod
    def move(self, x, y):
        ...