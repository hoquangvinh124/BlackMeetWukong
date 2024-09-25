from PyQt6.QtWidgets import QApplication, QMainWindow

from MainUI import Ui_MainWindow

app=QApplication([])
myWindow=Ui_MainWindow()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()