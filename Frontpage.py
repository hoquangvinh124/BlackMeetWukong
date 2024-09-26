from PyQt6.QtWidgets import QMainWindow, QMenu
from PyQt6.QtGui import QAction
from MainUI import Ui_MainWindow

import psycopg2

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

# Ket noi voi database
    def connection(self):
        connection = psycopg2.connect(
            user="sql12733511",
            password="mật_khẩu",  # Thay bằng mật khẩu của bạn
            host="localhost",  # Hoặc IP của server
            port="5432",  # Port mặc định của PostgreSQL
            database="tên_database"  # Thay bằng tên database
                )


