import os
from collections import Counter

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow

from libs.Dataconnector import DataConnector
from ui.Khach_hang.thanhtoan.Thanhtoan import Ui_MainWindow


class ThanhtoanExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.SignalandSlots()
        self.dc = DataConnector()
        self.Order = self.dc.get_all_orders()
        self.products = self.Order[len(self.Order) - 1].products
        self.show_hoadon()
        # Xác định thư mục hiện tại của file Python
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Nối đường dẫn đến file icon
        icon_path = os.path.join(current_dir, "..", "..", "..", "images", "skibidi.png")
        # Load icon
        icon = QtGui.QIcon(icon_path)
        self.MainWindow.setWindowIcon(icon)
    def show(self):
        self.MainWindow.show()
    def SignalandSlots(self):
        self.Xacnhanbutton.clicked.connect(self.Xacnhanthanhtoan)
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def show_hoadon(self):
        # Xóa dữ liệu cũ khỏi bảng
        self.hoadonthanhtoanwidget.setRowCount(0)

        # Đếm số lượng từng sản phẩm
        product_soluong = Counter()
        product_prices = {}  # Lưu giá của từng sản phẩm
        total_price = 0
        for product in self.products:
            name, price = product.rsplit(":", 1)  # Tách tên sản phẩm và giá
            product_soluong[name] += 1  # Đếm số lượng sản phẩm
            product_prices[name] = price.strip()  # Lưu giá (loại bỏ khoảng trắng nếu có)
            total_price += int(price)
        # Hiển thị sản phẩm duy nhất trong bảng
        for row, name in enumerate(product_soluong):
            parts = name.split()  # Tách tên sản phẩm
            product_ten = QTableWidgetItem(" ".join(parts[:-1]))  # Lấy tên sản phẩm (bỏ size)
            product_size = QTableWidgetItem(parts[-1])  # Lấy size (phần cuối)
            product_dongia = QTableWidgetItem(product_prices[name])  # Lấy giá
            product_count = QTableWidgetItem(str(product_soluong[name]))  # Lấy số lượng

            # Thêm dữ liệu vào bảng
            self.hoadonthanhtoanwidget.insertRow(row)
            self.hoadonthanhtoanwidget.setItem(row, 0, product_ten)
            self.hoadonthanhtoanwidget.setItem(row, 1, product_size)
            self.hoadonthanhtoanwidget.setItem(row, 2, product_dongia)
            self.hoadonthanhtoanwidget.setItem(row, 3, product_count)
        #Thành tiền
        self.Thanhtien.setText(str(total_price) + " VNĐ")
    def Xacnhanthanhtoan(self):
        from ui.Khach_hang.thanhtoan.XacnhanthanhtoanExt import XacnhanthanhtoanExt
        self.MainWindow.hide()
        self.quanly_window = QMainWindow()
        self.quanly_ui = XacnhanthanhtoanExt()
        self.quanly_ui.setupUi(self.quanly_window)
        self.quanly_window.show()