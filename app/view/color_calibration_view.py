from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtGui import QIcon
from app.controller.color_calibration_controller import ColorCalibrationController


class ColorCalibrationView(QtWidgets.QDialog):
    color_calibration_controller = ColorCalibrationController()
    button_size = 100

    def __init__(self, nb_marty, parent=None):
        super(ColorCalibrationView, self).__init__(parent)
        self.nb_marty = nb_marty
        self.setWindowTitle("Calibration des couleurs pour marty "+ str(nb_marty))
        self.setGeometry(0, 0, 200, 100)

        self.hLayout = QHBoxLayout(self)

        # Create the grid layout
        grid_layout_widget_caliber = QWidget(self)
        self.setGeometry(0, 0, 200, 100)
        grid_layout_caliber = QGridLayout(grid_layout_widget_caliber)

        self.b_black = QPushButton("", self)
        self.b_black.setStyleSheet("background-image:url('../public/black.png'); margin:0;")
        self.b_black.setFixedSize(self.button_size,self.button_size)
        self.b_black.setIcon(QIcon("../public/black.png"))
        self.b_black.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_black, 0, 0)

        self.b_dark_blue = QPushButton("", self)
        self.b_dark_blue.setStyleSheet("background-image:url('../public/dark_blue.png'); margin:0;")
        self.b_dark_blue.setFixedSize(self.button_size,self.button_size)
        self.b_dark_blue.setIcon(QIcon("../public/dark_blue.png"))
        self.b_dark_blue.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_dark_blue, 0, 1)

        self.b_green = QPushButton("", self)
        self.b_green.setStyleSheet("background-image:url('../public/green.png'); margin:0;")
        self.b_green.setFixedSize(self.button_size,self.button_size)
        self.b_green.setIcon(QIcon("../public/green.png"))
        self.b_green.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_green, 0, 2)

        self.b_light_blue = QPushButton("", self)
        self.b_light_blue.setStyleSheet("background-image:url('../public/light_blue.png'); margin:0;")
        self.b_light_blue.setFixedSize(self.button_size,self.button_size)
        self.b_light_blue.setIcon(QIcon("../public/light_blue.png"))
        self.b_light_blue.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_light_blue, 1, 0)

        self.b_pink = QPushButton("", self)
        self.b_pink.setStyleSheet("background-image:url('../public/pink.png'); margin:0;")
        self.b_pink.setFixedSize(self.button_size,self.button_size)
        self.b_pink.setIcon(QIcon("../public/pink.png"))
        self.b_pink.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_pink, 1, 1)

        self.b_red = QPushButton("", self)
        self.b_red.setStyleSheet("background-image:url('../public/red.png'); margin:0;")
        self.b_red.setFixedSize(self.button_size,self.button_size)
        self.b_red.setIcon(QIcon("../public/red.png"))
        self.b_red.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_red, 1, 2)

        self.b_yellow = QPushButton("", self)
        self.b_yellow.setStyleSheet("background-image:url('../public/yellow.png'); margin:0;")
        self.b_yellow.setFixedSize(self.button_size,self.button_size)
        self.b_yellow.setIcon(QIcon("../public/yellow.png"))
        self.b_yellow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_yellow, 2, 1)

        self.b_black.clicked.connect(lambda _: self.on_b_color_click("black"))
        self.b_dark_blue.clicked.connect(lambda _: self.on_b_color_click("dark_blue"))
        self.b_green.clicked.connect(lambda _: self.on_b_color_click("green"))
        self.b_light_blue.clicked.connect(lambda _: self.on_b_color_click("light_blue"))
        self.b_pink.clicked.connect(lambda _: self.on_b_color_click("pink"))
        self.b_red.clicked.connect(lambda _: self.on_b_color_click("red"))
        self.b_yellow.clicked.connect(lambda _: self.on_b_color_click("yellow"))



        self.hLayout.addWidget(grid_layout_widget_caliber, QtCore.Qt.AlignmentFlag.AlignCenter)



    def on_b_color_click(self, color):
        self.color_calibration_controller.calibrate(color, self.nb_marty)

    def on_ok(self):
        self.close()

    def on_close(self):
        self.close()