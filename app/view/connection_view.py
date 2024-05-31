import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialogButtonBox
from app.controller.connection_controller import ConnectionController
from app.view.mainwindow_view import MainWindowView


class ConnectionView(QtWidgets.QDialog ):

    def __init__(self):
        super().__init__()
        uic.loadUi("view/connectionWindow_view.ui", self)
        self.connection_controller = ConnectionController()

        self.buttonBox.accepted.connect(self.on_ok)
        self.buttonBox.rejected.connect(self.on_close)


    def on_ok(self):
        '''
        success = self.connection_controller.connect(self.IPInput.text())

        if(success == "success"):
            uic.loadUi("view/mainwindow_view.ui", self)

        if(success == "failed") :
            print("echec")'''
        print('baba')


    def on_close(self):
        self.close()