from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from app.controller.directional_arrows_controller import DirectionalArrowsController

class DirectionalArrowsView(QWidget):
    directional_arrows_controller = DirectionalArrowsController()

    def __init__(self, parent=None):
        super(DirectionalArrowsView, self).__init__(parent)

        self.setWindowTitle("Directional Arrows")
        self.setGeometry(0, 0, 400, 300)

        # Create the grid layout
        gridLayoutWidget = QWidget(self)
        gridLayoutWidget.setGeometry(30, 20, 325, 251)
        gridLayout = QGridLayout(gridLayoutWidget)

        # Add buttons to the layout with icons
        self.b_left = QPushButton("", self)
        self.b_left.setIcon(QIcon("../public/left-arrow.png"))
        self.b_left.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayout.addWidget(self.b_left, 1, 0)

        self.b_right = QPushButton("", self)
        self.b_right.setIcon(QIcon("../public/right-arrow.png"))
        self.b_right.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayout.addWidget(self.b_right, 1, 2)

        self.b_forw = QPushButton("", self)
        self.b_forw.setIcon(QIcon("../public/forw-arrow.png"))
        self.b_forw.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayout.addWidget(self.b_forw, 0, 1)

        self.b_forw_right = QPushButton("", self)
        self.b_forw_right.setIcon(QIcon("../public/up-right-arrow.png"))
        self.b_forw_right.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayout.addWidget(self.b_forw_right, 0, 2)

        self.b_back = QPushButton("", self)
        self.b_back.setIcon(QIcon("../public/back-arrow.png"))
        self.b_back.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayout.addWidget(self.b_back, 2, 1)

        self.b_forw_left = QPushButton("", self)
        self.b_forw_left.setIcon(QIcon("../public/up-left-arrow.png"))
        self.b_forw_left.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gridLayout.addWidget(self.b_forw_left, 0, 0)

        
        # Connect signals to slots
        self.b_forw.clicked.connect(self.on_b_forw_click)
        self.b_back.clicked.connect(self.on_b_back_click)
        self.b_left.clicked.connect(self.on_b_left_click)
        self.b_right.clicked.connect(self.on_b_right_click)
        self.b_forw_left.clicked.connect(self.on_b_forw_left_click)
        self.b_forw_right.clicked.connect(self.on_b_forw_right_click)

        self.b_forw.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.b_back.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.b_left.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.b_right.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.b_forw_left.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.b_forw_right.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.b_forw.installEventFilter(self)
        self.b_back.installEventFilter(self)
        self.b_left.installEventFilter(self)
        self.b_right.installEventFilter(self)
        self.b_forw_left.installEventFilter(self)
        self.b_forw_right.installEventFilter(self)

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

    def eventFilter(self, obj, event):
        if event.type() == 7:  # 6 corresponds au type d'événement KeyPress
            key = event.key()
            if key == Qt.Key.Key_Up or key == Qt.Key.Key_Z:
                self.on_b_forw_click()
            elif key == Qt.Key.Key_Down or key == Qt.Key.Key_S:
                self.on_b_back_click()
            elif key == Qt.Key.Key_Left or key == Qt.Key.Key_Q:
                self.on_b_left_click()
            elif key == Qt.Key.Key_Right or key == Qt.Key.Key_D:
                self.on_b_right_click()
            elif key == Qt.Key.Key_Up + Qt.Key.Key_Left or key == Qt.Key.Key_A:
                self.on_b_forw_left_click()
            elif key == Qt.Key.Key_Up + Qt.Key.Key_Right or key == Qt.Key.Key_E:
                self.on_b_forw_right_click()
            elif key == Qt.Key.Key_Backspace:
                self.directional_arrows_controller.hi()
            return True
        return super().eventFilter(obj, event)