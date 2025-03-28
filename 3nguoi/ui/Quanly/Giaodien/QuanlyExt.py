import os

from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QInputDialog

from libs.Dataconnector import DataConnector
from ui.Quanly.Giaodien.Quanly import Ui_MainWindow
from ui.Quanly.LichSuHoaDon.LichsuhoadonExt import LichsuhoadonExt
from ui.Quanly.QuanLyMenu.MenuExt import MenuExt
from ui.Quanly.QuanLyNhanVien.MainWindowEx import MainWindowEx
from ui.Quanly.ThongKeWindow.ThongkeExt import ThongkeExt


class QuanlyExt(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlots()
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Nối đường dẫn đến file icon
        icon_path = os.path.join(current_dir, ".." ,".." , "..", "images", "skibidi.png")  # Cập nhật thư mục đúng
        icon_back = os.path.join(current_dir, ".." ,".." , "..", "images", "Home.webp")
        background_icon = os.path.join(current_dir, ".." ,".." , "..", "images", "backround.png")
        # Load icon
        icon = QtGui.QIcon(icon_path)
        iconhome = QtGui.QIcon(icon_back)
        background = QtGui.QPixmap(background_icon)
        self.backbutton.setIcon(iconhome)
        self.MainWindow.setWindowIcon(icon)
        self.label.setPixmap(background)
    def show(self):
        self.MainWindow.show()
    def setupSignalandSlots(self):
        self.Hoadonbutton.clicked.connect(self.giaodienhoadon)
        self.Menubutton.clicked.connect(self.giaodienMenu)
        self.Thongkebutton.clicked.connect(self.giaodienthongke)
        self.Nhansubutton.clicked.connect(self.giaodiennhansu)
        self.backbutton.clicked.connect(self.back)
    def giaodienhoadon(self):
        self.MainWindow.close()
        # Tạo cửa sổ mới cho giao diện thanh toán
        self.quanlyhoadon_window = QMainWindow()
        self.quanlyhoadon_ui = LichsuhoadonExt()
        self.quanlyhoadon_ui.setupUi(self.quanlyhoadon_window)
        self.quanlyhoadon_window.show()
    def giaodienMenu(self):
        self.MainWindow.close()
        # Tạo cửa sổ mới cho giao diện thanh toán
        self.menu_window = QMainWindow()
        self.menu_ui = MenuExt()
        self.menu_ui.show()
    def giaodienthongke(self):
        self.MainWindow.close()
        # Tạo cửa sổ mới cho giao diện thanh toán
        self.thongke_window = QMainWindow()
        self.thongke_ui = ThongkeExt()
        self.thongke_ui.setupUi(self.thongke_window)
        self.thongke_window.show()
    def giaodiennhansu(self):
        self.MainWindow.close()
        # Tạo cửa sổ mới cho giao diện thanh toán
        self.nhansu_window = QMainWindow()
        self.nhansu_ui = MainWindowEx()
        self.nhansu_ui.setupUi(self.nhansu_window)
        self.nhansu_window.show()
    def back(self):
        self.MainWindow.hide()
        from ui.Login.LoginExt import LoginExt
        # Tạo cửa sổ mới cho giao diện quản lý
        self.modau_window = QMainWindow()
        self.modau_ui = LoginExt()
        self.modau_ui.setupUi(self.modau_window)
        self.modau_window.show()