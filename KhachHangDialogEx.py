
from KhachHangDialog import Ui_KhachHangDialog


class KhachHangDialogEx(Ui_KhachHangDialog):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
