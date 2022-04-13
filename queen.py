from figure import Figure

class Queen(Figure):

    def __init__(self, location_x, location_y, color):
        self.location_x = location_x
        self.location_y = location_y
        self.color = color

    def move(self):
        pass