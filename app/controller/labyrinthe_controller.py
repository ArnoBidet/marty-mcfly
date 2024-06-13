from app.model.marty import Marty

class LabyrintheController():
    def __init__(self):
        self.marty = Marty()

    def read_labyrinth(self,nb_marty):
        print("resolve")
        self.marty.read_labyrinth(nb_marty)
    
    def resolve(self,nb_marty):
        print("resolve")
        self.marty.labyrinthe(nb_marty)