from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy,QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from app.controller.directional_arrows_controller import DirectionalArrowsController

class DirectionalArrowsView(QWidget):
    directional_arrows_controller = DirectionalArrowsController()

    def __init__(self, mainWindow, parent=None):
        super(DirectionalArrowsView, self).__init__(parent)
        self.mainWindow = mainWindow
        self.setWindowTitle("Directional Arrows")
        self.setGeometry(0, 0, 400, 300)

        self.hLayout = QHBoxLayout(self)

        # Create the grid layout
        gridLayoutWidgetArrow = QWidget(self)
        gridLayoutWidgetArrow.setGeometry(30, 20, 325, 251)
        gridLayoutArrow = QGridLayout(gridLayoutWidgetArrow)


        # Add buttons to the layout with icons
        self.b_left = QPushButton("", self)
        self.b_left.setIcon(QIcon("../public/left-arrow.png"))
        self.b_left.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayoutArrow.addWidget(self.b_left, 1, 0)

        self.b_right = QPushButton("", self)
        self.b_right.setIcon(QIcon("../public/right-arrow.png"))
        self.b_right.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayoutArrow.addWidget(self.b_right, 1, 2)

        self.b_forw = QPushButton("", self)
        self.b_forw.setIcon(QIcon("../public/forw-arrow.png"))
        self.b_forw.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayoutArrow.addWidget(self.b_forw, 0, 1)

        self.b_forw_right = QPushButton("", self)
        self.b_forw_right.setIcon(QIcon("../public/up-right-arrow.png"))
        self.b_forw_right.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayoutArrow.addWidget(self.b_forw_right, 0, 2)

        self.b_back = QPushButton("", self)
        self.b_back.setIcon(QIcon("../public/back-arrow.png"))
        self.b_back.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayoutArrow.addWidget(self.b_back, 2, 1)

        self.b_forw_left = QPushButton("", self)
        self.b_forw_left.setIcon(QIcon("../public/up-left-arrow.png"))
        self.b_forw_left.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayoutArrow.addWidget(self.b_forw_left, 0, 0)

        
        # Connect signals to slots
        self.b_forw.clicked.connect(self.on_b_forw_click)
        self.b_back.clicked.connect(self.on_b_back_click)
        self.b_left.clicked.connect(self.on_b_left_click)
        self.b_right.clicked.connect(self.on_b_right_click)
        self.b_forw_left.clicked.connect(self.on_b_forw_left_click)
        self.b_forw_right.clicked.connect(self.on_b_forw_right_click)

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

        self.hLayout.addWidget(gridLayoutWidgetArrow)
        self.hLayout.addWidget(gridLayoutWidget)



    def on_b_forw_click(self):
        self.directional_arrows_controller.on_b_forw_click()

    def on_b_back_click(self):
        self.directional_arrows_controller.on_b_back_click()

    def on_b_left_click(self):
        self.directional_arrows_controller.on_b_left_click()

    def on_b_right_click(self):
        self.directional_arrows_controller.on_b_right_click()

    def on_b_forw_left_click(self):
        self.directional_arrows_controller.on_b_forw_left_click()

    def on_b_forw_right_click(self):
        self.directional_arrows_controller.on_b_forw_right_click()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Up:
            self.directional_arrows_controller.on_b_forw_click()
        elif event.key() == Qt.Key.Key_Down:
            self.directional_arrows_controller.on_b_back_click()
        elif event.key() == Qt.Key.Key_Left:
            self.directional_arrows_controller.on_b_left_click()
        elif event.key() == Qt.Key.Key_Right:
            self.directional_arrows_controller.on_b_right_click()
        elif event.key() == Qt.Key.Key_Up + Qt.Key.Key_Left:
            self.directional_arrows_controller.on_b_forw_left_click()
        elif event.key() == Qt.Key.Key_Up + Qt.Key.Key_Right:
            self.directional_arrows_controller.on_b_forw_right_click()


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

    def keyPressEvent(self, event):
        self.keyPressEvent(event)