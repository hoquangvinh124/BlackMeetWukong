from PyQt6.QtWidgets import QApplication, QMainWindow
from MainUI import Ui_MainWindow  # Giao diện được tạo từ Qt Designer
import resources# Tệp chứa tài nguyên từ .qrc

app = QApplication([])

# Tạo cửa sổ QMainWindow
mainWindow = QMainWindow()

# Tạo đối tượng giao diện từ Ui_MainWindow
ui = Ui_MainWindow()

# Thiết lập giao diện cho cửa sổ chính
ui.setupUi(mainWindow)

# Hiển thị cửa sổ
mainWindow.show()

# Chạy ứng dụng
app.exec()
