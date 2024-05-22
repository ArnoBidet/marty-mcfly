import sys
from PyQt6 import QtWidgets, uic
from controller.directional_arrows import DirectionalArrows

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("app/view/mainwindow.ui", self)

        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())