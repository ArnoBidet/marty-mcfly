from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget, QGridLayout, QPushButton, QSizePolicy, QDialogButtonBox, \
    QLineEdit
from PyQt6.QtGui import QIcon
from app.controller.labyrinthe_controller import LabyrintheController
from app.controller.connection_controller import ConnectionController
from app.view.color_calibration_view import ColorCalibrationView


class LabyrintheView(QtWidgets.QDialog):
    labyrinthe_controller = LabyrintheController()
    connection_controller = ConnectionController()

    button_size = 100

    def __init__(self, parent=None):
        super(LabyrintheView, self).__init__(parent)
        self.setWindowTitle("Calibration des couleurs")
        self.setGeometry(0, 0, 200, 100)

        self.hLayout = QHBoxLayout(self)

        grid_layout_widget_labyrinthe = QWidget(self)
        grid_layout_widget_labyrinthe.setGeometry(0, 0, 200, 100)
        grid_layout_labyrinthe = QGridLayout(grid_layout_widget_labyrinthe)

        self.l_marty_0 = QLabel("Marty 1", self)
        self.l_marty_0.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_labyrinthe.addWidget(self.l_marty_0, 0, 0)

        self.b_calibrate_marty_0 = QPushButton("", self)
        self.b_calibrate_marty_0.setStyleSheet("background-image:url('../public/calibrate.png'); margin:0;")
        self.b_calibrate_marty_0.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_calibrate_marty_0, 4, 0)

        self.b_scan_marty_0 = QPushButton("", self)
        self.b_scan_marty_0.setStyleSheet("background-image:url('../public/scan.png'); margin:0;")
        self.b_scan_marty_0.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_scan_marty_0, 5, 0)

        self.l_marty_1 = QLabel("Marty 2", self)
        self.l_marty_1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_labyrinthe.addWidget(self.l_marty_1, 0, 1)

        self.textConnexion = QLabel("Veuillez rentrer l'ip de marty", self)
        self.textConnexion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        grid_layout_labyrinthe.addWidget(self.textConnexion, 1, 1)

        # Add the IP input line edit
        self.IPInput = QLineEdit("192.168.252.182", self)
        self.IPInput.setMaxLength(15)
        self.IPInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        grid_layout_labyrinthe.addWidget(self.IPInput, 2, 1)

        # Add the button box
        self.b_connect_marty_1 = QPushButton("Connecter", self)
        grid_layout_labyrinthe.addWidget(self.b_connect_marty_1, 3, 1)

        self.b_calibrate_marty_1 = QPushButton("", self)
        self.b_calibrate_marty_1.setStyleSheet("background-image:url('../public/calibrate.png'); margin:0;")
        self.b_calibrate_marty_1.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_calibrate_marty_1, 4, 1)

        self.b_scan_marty_1 = QPushButton("", self)
        self.b_scan_marty_1.setStyleSheet("background-image:url('../public/scan.png'); margin:0;")
        self.b_scan_marty_1.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_scan_marty_1, 5, 1)

        self.b_resolve = QPushButton("Résoudre", self)
        grid_layout_labyrinthe.addWidget(self.b_resolve, 6, 0)

        self.b_calibrate_marty_0.clicked.connect(lambda _: self.b_calibrate(0))
        self.b_calibrate_marty_1.clicked.connect(lambda _: self.b_calibrate(1))
        self.b_scan_marty_0.clicked.connect(lambda _: self.b_scan(0))
        self.b_scan_marty_1.clicked.connect(lambda _: self.b_scan(1))
        self.b_resolve.clicked.connect(lambda _: self.b_resolve())
        self.b_connect_marty_1.clicked.connect(lambda _:self.b_connect())


        self.hLayout.addWidget(grid_layout_widget_labyrinthe)

    def b_calibrate(self, nb_marty):
        color_calibration_view = ColorCalibrationView(nb_marty)
        color_calibration_view.setModal(True)
        color_calibration_view.show()

    def b_scan(self, nb_marty):
        pass

    def b_connect(self):
        pass

    def b_disconnect(self):
        pass

    def on_ok(self):
        self.close()

    def on_close(self):
        self.close()
