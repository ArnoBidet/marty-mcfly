from PyQt6 import QtWidgets, uic
from controller.connection_controller import ConnectionController
from view.action_view import ActionView
from view.directional_arrows_view import DirectionalArrowsView


class ConnectionView(QtWidgets.QDialog ):
    connection_controller = ConnectionController()

    def __init__(self,mainWindow ,parent=None):
        super(ConnectionView, self).__init__(parent)
        self.mainWindow = mainWindow
        uic.loadUi("view/connection_view.ui", self)

        self.buttonBox.accepted.connect(self.on_ok)
        self.buttonBox.rejected.connect(self.on_close)


    def on_ok(self):
        success = self.connection_controller.connect(self.IPInput.text())

        if(success == "success"):
            directional_arrows_view = DirectionalArrowsView()
            actionView = ActionView()
            self.mainWindow.resize(directional_arrows_view.width() + actionView.height() + 100, directional_arrows_view.height())

            self.mainWindow.hLayout.addWidget(directional_arrows_view)
            self.mainWindow.hLayout.addWidget(actionView)

        if(success == "failed") :
            connectionView = ConnectionView(self)
            connectionView.textConnexion.setText("Erreur lors de la connexion")
            self.mainWindow.resize(connectionView.width(), connectionView.height())
            self.mainWindow.hLayout.addWidget(connectionView)


    def on_close(self):
        self.close()