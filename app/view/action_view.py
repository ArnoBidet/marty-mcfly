from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from app.controller.action_controller import ActionController


class ActionView(QWidget):
    directional_arrows_controller = ActionController()

    def __init__(self, parent=None):
        super(ActionView, self).__init__(parent)
        
        uic.loadUi("view/action_view.ui", self)

        
        # Connect signals to slots
        self.b_stand_straight.clicked.connect(self.on_b_stand_straight)
        self.b_dance.clicked.connect(self.on_b_dance)
        self.b_celebrate.clicked.connect(self.on_b_celebrate)
        self.b_wave_left.clicked.connect(self.on_b_wave_left)
        self.b_wave_right.clicked.connect(self.on_b_wave_right)
        self.b_hello.clicked.connect(self.on_b_hello)
        self.b_shoot_right.clicked.connect(self.on_b_shoot_right)
        self.b_shoot_left.clicked.connect(self.on_b_shoot_left)

        

    def on_b_stand_straight(self):
        self.directional_arrows_controller.on_b_stand_straight()

    def on_b_dance(self):
        self.directional_arrows_controller.on_b_dance()

    def on_b_celebrate(self):
        self.directional_arrows_controller.on_b_celebrate()

    def on_b_wave_left(self):
        self.directional_arrows_controller.on_b_wave_left()

    def on_b_wave_right(self):
        self.directional_arrows_controller.on_b_wave_right()

    def on_b_hello(self):
        self.directional_arrows_controller.on_b_hello()

    def on_b_shoot_right(self):
        self.directional_arrows_controller.on_b_shoot_right()
    
    def on_b_shoot_left(self):
        self.directional_arrows_controller.on_b_shoot_left()
