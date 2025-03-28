import os

from PyQt6 import QtGui
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow

from ui.Khach_hang.thanhtoan.Xacnhanthanhtoan import Ui_MainWindow
from ui.Login.LoginExt import LoginExt


class XacnhanthanhtoanExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.Dangkybutton.clicked.connect(self.Momo)
        self.HomeButton.clicked.connect(self.Home)
        # Xác định thư mục hiện tại của file Python
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Nối đường dẫn đến file icon
        icon_path = os.path.join(current_dir, "..", "..", "..", "images", "skibidi.png")
        icon_back = os.path.join(current_dir, "..", "..", "..", "images", "Home.webp")
        momoicon = os.path.join(current_dir, "..", "..", "..", "images", "Screenshot 2025-03-22 174809.png")
        QRicon = os.path.join(current_dir, "..", "..", "..", "images", "Screenshot 2025-03-22 174353.png")
        dangky = os.path.join(current_dir, "..", "..", "..", "images", "Screenshot 2025-03-22 180342.png")
        # Load icon
        icon = QtGui.QIcon(icon_path)
        iconHome = QtGui.QIcon(icon_back)
        self.MainWindow.setWindowIcon(icon)
        self.HomeButton.setIcon(iconHome)
        self.label.setPixmap(QtGui.QPixmap(momoicon))
        self.label_2.setPixmap(QtGui.QPixmap(QRicon))
        self.Dangkybutton.setIcon(QtGui.QIcon(dangky))
    def show(self):
        self.MainWindow.show()
    def Momo(self):
        url = QUrl("https://www.momo.vn/tro-thu-tai-chinh")
        QDesktopServices.openUrl(url)
    def Home(self):
        self.MainWindow.hide()
        self.Login_window = QMainWindow()
        self.Login_ui = LoginExt()
        self.Login_ui.setupUi(self.Login_window)
        self.Login_window.show()