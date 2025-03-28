import os

from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow
from ui.Khach_hang.Menu.MainWindowMenuOrderExt import MainWindowMenuOrderExt
from ui.Login.Login import Ui_MainWindow
from ui.Quanly.LoginQuanly.LoginQuanlyExt import LoginQuanlyExt

class LoginExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlots()
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Nối đường dẫn đến file icon
        icon_path = os.path.join(current_dir, ".." , "..", "images", "skibidi.png")  # Cập nhật thư mục đúng
        background = os.path.join(current_dir, "..", "..", "images", "backround.png")
        # Load icon
        icon = QtGui.QIcon(icon_path)
        self.label_10.setPixmap(QtGui.QPixmap(background))
        # Đặt icon cho cửa sổ
        self.MainWindow.setWindowIcon(icon)

    def show(self):
        self.MainWindow.show()
    def setupSignalandSlots(self):
        self.quanlybutton.clicked.connect(self.giaodienquanly)
        self.khachhangbutton.clicked.connect(self.khachhanggiaodien)
    def giaodienquanly(self):
        self.MainWindow.close()
        # Tạo cửa sổ mới cho giao diện quản lý
        self.quanlylogin_window = QMainWindow()
        self.quanlylogin_ui = LoginQuanlyExt()
        self.quanlylogin_ui.setupUi(self.quanlylogin_window)
        self.quanlylogin_window.show()
    def khachhanggiaodien(self):
        self.MainWindow.close()
        # Tạo cửa sổ mới cho giao diện quản lý
        self.menu_window = QMainWindow()
        self.menu_ui = MainWindowMenuOrderExt()
        self.menu_ui.setupUi(self.menu_window)
        self.menu_window.show()
