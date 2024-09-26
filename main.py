from PyQt6.QtWidgets import QApplication, QMainWindow
from MainUI import Ui_MainWindow
import resources_rc

app = QApplication([])  # Initialize the application
MainWindow = QMainWindow()  # Create an instance of QMainWindow
ui = Ui_MainWindow()  # Create an instance of the UI class
ui.setupUi(MainWindow)  # Set up the UI on the QMainWindow instance
MainWindow.show()  # Show the QMainWindow
app.exec()  # Execute the application
