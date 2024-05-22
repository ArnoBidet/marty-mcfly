from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class DirectionalArrows(QWidget):
    def __init__(self, parent=None):
        super(DirectionalArrows, self).__init__(parent)
        
        uic.loadUi("app/view/directional_arrows.ui", self)

        
        # Connect signals to slots
        self.b_forw.clicked.connect(self.on_b_forw_click)
        self.b_back.clicked.connect(self.on_b_back_click)
        self.b_left.clicked.connect(self.on_b_left_click)
        self.b_right.clicked.connect(self.on_b_right_click)
        self.b_forw_left.clicked.connect(self.on_b_forw_left_click)
        self.b_forw_right.clicked.connect(self.on_b_forw_right_click)

        

    def on_b_forw_click(self):
        print("Button 'forward' clicked!")

    def on_b_back_click(self):
        print("Button 'backward' clicked!")

    def on_b_left_click(self):
        print("Button 'left' clicked!")

    def on_b_right_click(self):
        print("Button 'right' clicked!")

    def on_b_forw_left_click(self):
        print("Button 'forward-left' clicked!")

    def on_b_forw_right_click(self):
        print("Button 'forward-right' clicked!")