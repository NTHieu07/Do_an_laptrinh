import os

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from libs.Dataconnector import DataConnector
from ui.Quanly.Giaodien.QuanlyExt import QuanlyExt
from ui.Quanly.LoginQuanly.LoginQuanly import Ui_MainWindow


class LoginQuanlyExt(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.emp = self.dc.get_all_employees()
        self.o = 1 # để dành dùng cho thằng password close open
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonLogin.clicked.connect(self.loginemp)
        self.backbutton.clicked.connect(self.back)
        self.HideAndOpenPass.clicked.connect(self.PassOpen)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Nối đường dẫn đến file icon
        icon_path = os.path.join(current_dir, ".." ,".." , "..", "images", "skibidi.png")  # Cập nhật thư mục đúng
        icon_back = os.path.join(current_dir, ".." ,".." , "..", "images", "back.png")
        self.icon_open = os.path.join(current_dir, ".." ,"..",".." ,"images", "OpenPassword.webp")
        self.icon_close = os.path.join(current_dir, ".." ,"..", ".." ,"images", "ClosePassword.webp")

        # Load icon
        icon = QtGui.QIcon(icon_path)
        iconback = QtGui.QIcon(icon_back)

        self.HideAndOpenPass.setIcon(QtGui.QIcon(self.icon_close))
        self.backbutton.setIcon(iconback)
        self.MainWindow.setWindowIcon(icon)
    def show(self):
        self.MainWindow.show()
    def loginemp(self):
        emp_id = self.IDlineEdit.text()
        password = self.lineEditPassword.text()

        # Tìm nhân viên có id khớp và chức vụ là "Quản Lý"
        found_emp = None
        for e in self.emp:
            if e.id == emp_id and e.chuc_vu == "Quản Lý":
                found_emp = e
                break

        if found_emp and password == "1111":
            self.MainWindow.close()
            # Tạo cửa sổ mới cho giao diện quản lý
            self.quanly_window = QMainWindow()
            self.quanly_ui = QuanlyExt()
            self.quanly_ui.setupUi(self.quanly_window)
            self.quanly_window.show()
        else:
            msg = QMessageBox(self.MainWindow)
            msg.setWindowTitle("Lỗi đăng nhập!")
            msg.setText("Id hoặc mật khẩu không đúng")
            msg.exec()
    def back(self):
        self.MainWindow.hide()
        from ui.Login.LoginExt import LoginExt
        # Tạo cửa sổ mới cho giao diện quản lý
        self.modau_window = QMainWindow()
        self.modau_ui = LoginExt()
        self.modau_ui.setupUi(self.modau_window)
        self.modau_window.show()
    def PassOpen(self):
        if self.o == 1:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.HideAndOpenPass.setIcon(QtGui.QIcon(self.icon_open))
            self.o = 0
        elif self.o == 0:
            self.PassClose()
    def PassClose(self):
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.HideAndOpenPass.setIcon(QtGui.QIcon(self.icon_close))
        self.o = 1