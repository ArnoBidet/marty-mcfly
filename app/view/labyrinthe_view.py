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
        grid_layout_labyrinthe.addWidget(self.l_marty_0, 0, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.b_calibrate_marty_0 = QPushButton("", self)
        self.b_calibrate_marty_0.setStyleSheet("background-image:url('../public/calibrate.png');")
        self.b_calibrate_marty_0.setFixedSize(self.button_size, self.button_size)
        grid_layout_labyrinthe.setAlignment(self.b_calibrate_marty_0, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid_layout_labyrinthe.addWidget(self.b_calibrate_marty_0, 4, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.b_scan_marty_0 = QPushButton("", self)
        self.b_scan_marty_0.setStyleSheet("background-image:url('../public/scan.png'); margin:0;")
        self.b_scan_marty_0.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_scan_marty_0, 5, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.l_marty_1 = QLabel("Marty 2", self)
        self.l_marty_1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_labyrinthe.addWidget(self.l_marty_1, 0, 2, QtCore.Qt.AlignmentFlag.AlignCenter)


        self.l_marty_0_status = QLabel("", self)
        self.l_marty_0_status.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        grid_layout_labyrinthe.addWidget(self.l_marty_0_status, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        # Add the IP input line edit
        self.IPInput = QLineEdit("192.168.0.116", self)
        font = self.IPInput.font()  # lineedit current font
        font.setPointSize(10)  # change it's size
        self.IPInput.setFont(font)
        self.IPInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        grid_layout_labyrinthe.addWidget(self.IPInput, 2, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        # Add the button box
        self.b_connect_marty_1 = QPushButton("Connecter", self)
        grid_layout_labyrinthe.addWidget(self.b_connect_marty_1, 3, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.b_calibrate_marty_1 = QPushButton("", self)
        self.b_calibrate_marty_1.setStyleSheet("background-image:url('../public/calibrate.png'); margin:0;")
        self.b_calibrate_marty_1.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_calibrate_marty_1, 4, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.b_scan_marty_1 = QPushButton("", self)
        self.b_scan_marty_1.setStyleSheet("background-image:url('../public/scan.png'); margin:0;")
        self.b_scan_marty_1.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_scan_marty_1, 5, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.b_resolve = QPushButton("Résoudre", self)
        self.b_resolve.setStyleSheet("background-image:url('../public/solve.png'); margin:0;")
        self.b_resolve.setFixedSize(self.button_size,self.button_size)
        grid_layout_labyrinthe.addWidget(self.b_resolve, 6, 1, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.b_calibrate_marty_0.clicked.connect(lambda _: self.b_calibrate(0))
        self.b_calibrate_marty_1.clicked.connect(lambda _: self.b_calibrate(1))
        self.b_scan_marty_0.clicked.connect(lambda _: self.b_scan(0))
        self.b_scan_marty_1.clicked.connect(lambda _: self.b_scan(1))
        self.b_resolve.clicked.connect(lambda _: self.b_resolve())
        self.b_connect_marty_1.clicked.connect(lambda _:self.b_connect())


        self.hLayout.addWidget(grid_layout_widget_labyrinthe, QtCore.Qt.AlignmentFlag.AlignCenter)

    def b_calibrate(self, nb_marty):
        color_calibration_view = ColorCalibrationView(nb_marty)
        color_calibration_view.setModal(True)
        color_calibration_view.show()

    def b_scan(self, nb_marty):
        self.labyrinthe_controller.read_labyrinth(nb_marty)

    def b_connect(self):
        success = self.connection_controller.connect(self.IPInput.text(),1)

        if (success == "success"):
            self.l_marty_0_status.setText("connecté")

        if (success == "failed"):
            self.l_marty_0_status.setText("échec")
            self.IPInput.setText(self.IPInput.text())

        pass

    def b_disconnect(self):
        pass

    def on_ok(self):
        self.close()

    def on_close(self):
        self.close()
