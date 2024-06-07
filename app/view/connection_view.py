from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import  QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
from app.controller.connection_controller import ConnectionController
from app.view.action_view import ActionView


class ConnectionView(QtWidgets.QDialog ):
    connection_controller = ConnectionController()

    def __init__(self,mainWindow ,parent=None):
        super(ConnectionView, self).__init__(parent)
        self.mainWindow = mainWindow
        
        self.setWindowTitle("Dialog")
        self.setGeometry(0, 0, 400, 317)

        # Create the main layout
        main_layout = QVBoxLayout(self)

        # Add the label
        self.textConnexion = QLabel("Veuillez rentrer l'ip de marty", self)
        self.textConnexion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.textConnexion)

        # Add the IP input line edit
        self.IPInput = QLineEdit("192.168.0.0", self)
        self.IPInput.setMaxLength(15)
        self.IPInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.IPInput)

        # Add the button box
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Connecter", QDialogButtonBox.ButtonRole.YesRole)
        self.buttonBox.addButton("Fermer", QDialogButtonBox.ButtonRole.NoRole)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        main_layout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.on_ok)
        self.buttonBox.rejected.connect(self.on_close)


    def on_ok(self):
        success = self.connection_controller.connect(self.IPInput.text())

        if(success == "success"):
            action_view = ActionView(self.mainWindow)
            self.mainWindow.resize(1000, 800)
            self.mainWindow.hLayout.addWidget(action_view)

        if(success == "failed") :
            connectionView = ConnectionView(self, self.mainWindow)
            connectionView.textConnexion.setText("Erreur lors de la connexion")
            self.mainWindow.resize(connectionView.width(), connectionView.height())
            self.mainWindow.hLayout.addWidget(connectionView)


    def on_close(self):
        self.close()