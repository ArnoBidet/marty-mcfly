from PyQt6 import uic
from PyQt6 import QtWidgets

from app.view.connection_view import ConnectionView
from app.view.directional_arrows_view import DirectionalArrowsView


class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        uic.loadUi("view/mainwindow_view.ui", self)
        directional_arrows_view = DirectionalArrowsView()
        connectionView = ConnectionView(self)
        self.resize(connectionView.width(), connectionView.height())
        self.hLayout.addWidget(connectionView)
