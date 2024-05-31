from PyQt6 import QtWidgets, uic
from view.directional_arrows_view import DirectionalArrowsView
from view.action_view import ActionView
class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        uic.loadUi("app/view/mainwindow_view.ui", self)
        directional_arrows_view = DirectionalArrowsView()
        actionView = ActionView()
        self.resize(directional_arrows_view.width()+actionView.height()+100,directional_arrows_view.height())
        
        self.hLayout.addWidget(directional_arrows_view)
        self.hLayout.addWidget(actionView)

    