from PyQt6.QtWidgets import QApplication, QMainWindow
from MainUI import Ui_MainWindow

app = QApplication([])

# Tạo đối tượng QMainWindow
mainWindow = QMainWindow()

# Tạo đối tượng giao diện Ui_MainWindow
ui = Ui_MainWindow()

# Thiết lập giao diện cho QMainWindow
ui.setupUi(mainWindow)

# Hiển thị cửa sổ chính
mainWindow.show()

# Chạy ứng dụng
app.exec()
