import sys
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("app/view/mainwindow.ui")
window.show()
app.exec()