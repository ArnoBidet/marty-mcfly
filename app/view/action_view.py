from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6 import uic

from app.controller.action_controller import ActionController


class ActionView(QWidget):
    directional_arrows_controller = ActionController()

    def __init__(self, parent=None):
        super(ActionView, self).__init__(parent)

        self.setWindowTitle("Form")
        self.setGeometry(0, 0, 400, 300)

        # Create the grid layout
        gridLayoutWidget = QWidget(self)
        gridLayoutWidget.setGeometry(0, 30, 391, 231)
        gridLayout = QGridLayout(gridLayoutWidget)

        # Add buttons to the layout
        self.b_stand_straight = QPushButton("Stand straight", self)
        gridLayout.addWidget(self.b_stand_straight, 0, 0)

        self.b_dance = QPushButton("Dance", self)
        gridLayout.addWidget(self.b_dance, 0, 1)

        self.b_celebrate = QPushButton("Celebrate", self)
        gridLayout.addWidget(self.b_celebrate, 1, 0)

        self.b_wave_left = QPushButton("Wave left", self)
        gridLayout.addWidget(self.b_wave_left, 0, 2)

        self.b_wave_right = QPushButton("Wave right", self)
        gridLayout.addWidget(self.b_wave_right, 0, 3)

        self.b_hello = QPushButton("Hello", self)
        gridLayout.addWidget(self.b_hello, 1, 1)

        self.b_shoot_right = QPushButton("Shoot right", self)
        gridLayout.addWidget(self.b_shoot_right, 1, 2)

        self.b_shoot_left = QPushButton("Shoot left", self)
        gridLayout.addWidget(self.b_shoot_left, 1, 3)

        
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
