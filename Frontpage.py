from PyQt6.QtWidgets import QMainWindow, QMenu
from PyQt6.QtGui import QAction
from MainUI import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init()
        self.setupUi(self)
        self.setWindowTitle('SideBar Menu')

    #Hide Widget Menu
        self.icon_only_widget.setHiden(True)

    #Hide Dropdowns
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)