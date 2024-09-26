import sys

from PySide6.QtWidgets import QApplication, QMainWindow


from MainUI import Ui_MainWindow
import resources_rc
from Frontpage import MySideBar


app = QApplication(sys.argv)
window=MySideBar()
window.show()
app.exec()
