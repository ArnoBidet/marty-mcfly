from app.model.marty import Marty

class LabyrintheController():
    def __init__(self):
        self.marty = Marty()
    
    def resolve(nb_marty):
        print("resolve")
        self.marty.labyrinthe(nb_marty)