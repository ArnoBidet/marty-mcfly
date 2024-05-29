import sys
from PyQt6 import QtWidgets, uic

from app.model.ipFinder import IpFinder


class ConnectionWindow(QtWidgets.QDialog):  # Changer QMainWindow à QDialog
    def __init__(self):
        super().__init__()
        uic.loadUi("./connectionWindow.ui", self)

