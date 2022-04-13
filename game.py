
from turtle import update


class Game():

    def __init__(self):
        self._game_over = False

    def start(self):
        while not self._game_over:
            self.update()
            self.draw()
            
    def update(self):
        print("update")
        input("teď hráč zadá pohyb: ")
           
    def draw(self):
        print("teď se hra překreslí")