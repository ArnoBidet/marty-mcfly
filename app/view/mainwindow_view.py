from PyQt6 import QtWidgets, uic

class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        uic.loadUi("app/view/mainwindow_view.ui", self)