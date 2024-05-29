import sys
from PyQt6 import QtWidgets
from view.mainwindow_view import MainWindowView

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window_view = MainWindowView()
    main_window_view.show()
    sys.exit(app.exec())