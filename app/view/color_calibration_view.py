from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtGui import QIcon
from app.controller.color_calibration_controller import ColorCalibrationController



class ColorCalibrationView(QtWidgets.QDialog):
    color_calibration_controller = ColorCalibrationController()

    def __init__(self, parent=None):
        super(ColorCalibrationView, self).__init__(parent)
        self.setWindowTitle("Directional Arrows")
        self.setGeometry(0, 0, 400, 300)

        self.hLayout = QHBoxLayout(self)

        # Create the grid layout
        grid_layout_widget_caliber = QWidget(self)
        grid_layout_widget_caliber.setGeometry(30, 20, 325, 251)
        grid_layout_caliber = QGridLayout(grid_layout_widget_caliber)

        self.b_black = QPushButton("", self)
        self.b_black.setIcon(QIcon("../public/black.png"))
        self.b_black.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_black, 0, 0)

        self.b_dark_blue = QPushButton("", self)
        self.b_dark_blue.setIcon(QIcon("../public/dark_blue.png"))
        self.b_dark_blue.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_dark_blue, 0, 1)

        self.b_green = QPushButton("", self)
        self.b_green.setIcon(QIcon("../public/green.png"))
        self.b_green.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_green, 0, 2)

        self.b_light_blue = QPushButton("", self)
        self.b_light_blue.setIcon(QIcon("../public/light_blue.png"))
        self.b_light_blue.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_light_blue, 1, 0)

        self.b_pink = QPushButton("", self)
        self.b_pink.setIcon(QIcon("../public/pink.png"))
        self.b_pink.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_pink, 1, 1)

        self.b_red = QPushButton("", self)
        self.b_red.setIcon(QIcon("../public/red.png"))
        self.b_red.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_caliber.addWidget(self.b_red, 1, 2)

        self.b_yellow = QPushButton("", self)
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


    def on_b_color_click(self, color):
        self.color_calibration_controller.calibrate(color)

    def on_ok(self):
        self.close()

    def on_close(self):
        self.close()