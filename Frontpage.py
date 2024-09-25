from PyQt6.QtWidgets import QMainWindow, QMenu
from PyQt6.QtGui import QAction
from MainUI import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')