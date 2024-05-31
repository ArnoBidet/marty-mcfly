from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtCore import Qt
from controller.directional_arrows_controller import DirectionalArrowsController

class DirectionalArrowsView(QWidget):
    directional_arrows_controller = DirectionalArrowsController()

    def __init__(self, parent=None):
        super(DirectionalArrowsView, self).__init__(parent)
        
        uic.loadUi("view/directional_arrows_view.ui", self)

        
        # Connect signals to slots
        self.b_forw.clicked.connect(self.on_b_forw_click)
        self.b_back.clicked.connect(self.on_b_back_click)
        self.b_left.clicked.connect(self.on_b_left_click)
        self.b_right.clicked.connect(self.on_b_right_click)
        self.b_forw_left.clicked.connect(self.on_b_forw_left_click)
        self.b_forw_right.clicked.connect(self.on_b_forw_right_click)

        

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