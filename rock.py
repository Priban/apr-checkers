from figure import Figure

class Rock(Figure):

    def __init__(self, location_x, location_y, color):
        self.location_x = location_x
        self.location_y = location_y
        self.color = color

    def move(self):
        pass

    def promote_to_queen(self):
        pass