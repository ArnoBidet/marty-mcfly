from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from app.view.directional_arrows_view import DirectionalArrowsView
from app.view.connection_view import ConnectionView
from app.view.action_view import ActionView
class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        uic.loadUi("view/mainwindow_view.ui", self)
        connection_view = ConnectionView(self)
        self.resize(connection_view.width(), connection_view.height())
        self.hLayout.addWidget(connection_view)
        self.directional_arrows_view = DirectionalArrowsView()
        # self.actionView = ActionView()
        # self.resize(self.directional_arrows_view.width()+self.actionView.height()+100,self.directional_arrows_view.height())
        
        # self.hLayout.addWidget(self.directional_arrows_view)
        # self.hLayout.addWidget(self.actionView)
        
    def keyPressEvent(self, event):
        self.directional_arrows_view.keyPressEvent(event)
