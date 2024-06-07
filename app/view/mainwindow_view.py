from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from app.view.directional_arrows_view import DirectionalArrowsView
from app.view.connection_view import ConnectionView

class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()

        self.setWindowTitle("MainWindow")

        # Set central widget
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Create main vertical layout
        self.vLayout = QVBoxLayout(self.centralwidget)

        # Create horizontal layout
        self.hLayout = QHBoxLayout()

        # Add the horizontal layout to the vertical layout
        self.vLayout.addLayout(self.hLayout)

        connection_view = ConnectionView(self)
        self.resize(connection_view.width(), connection_view.height())
        self.hLayout.addWidget(connection_view)
        self.directional_arrows_view = DirectionalArrowsView()

    def keyPressEvent(self, event):
        self.directional_arrows_view.keyPressEvent(event)
