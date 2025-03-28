import functools
import os
from collections import Counter

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow

from libs.Dataconnector import DataConnector
from ui.Quanly.LichSuHoaDon.Lichsuhoadon import Ui_MainWindow


class LichsuhoadonExt(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.Order = self.dc.get_all_orders()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.background = os.path.join(current_dir, "..", "..", "..", "images", "backround.png")
        self.back = os.path.normpath(os.path.join(current_dir, "..", "..",".." , "images", "back.png"))
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlots()
        self.hienthilichsu()
        self.label_8.setPixmap(QtGui.QPixmap(self.background))
        self.HomeButton.setIcon(QtGui.QIcon(self.back))
    def setupSignalandSlots(self):
        self.HomeButton.clicked.connect(self.Home)


    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def hienthilichsu(self):
        self.clearLayout(self.verticalLayout_hoadon)
        for i in range(len(self.Order)):
            order=self.Order[i]
            btn=QPushButton(text=str(order.name) + " " +"||"+ " " + order.time.split(" ")[0])
            self.verticalLayout_hoadon.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet,order))
    def xem_chi_tiet(self , order):
        self.clearLayout(self.verticallayout_listmua)
        totalcost = 0
        # Đếm số lượng sản phẩm
        product_counter = Counter()
        product_prices = {}
        for product in order.products:
            name, price = product.rsplit(":", 1)  # Tách tên sản phẩm và giá
            price = int(price)
            product_counter[name] += 1
            product_prices[name] = price
            totalcost += price
        list = "\n".join(f"{count} {name} : {count*product_prices[name]} VNĐ" for name, count in product_counter.items())
        ql = QLabel(list)
        self.Tenkhachhang.setText(order.name)
        self.NgayMua.setText(order.time)
        self.verticallayout_listmua.addWidget(ql)
        self.Thanhtien.setText(str(totalcost) + " VNĐ")
        self.Thanhtien.setAlignment(Qt.AlignmentFlag.AlignRight)
    def Home(self):
        self.MainWindow.close()
        from ui.Quanly.Giaodien.QuanlyExt import QuanlyExt
        # Tạo cửa sổ mới cho giao diện quản lý
        self.quanly_window = QMainWindow()
        self.quanly_ui = QuanlyExt()
        self.quanly_ui.setupUi(self.quanly_window)
        self.quanly_window.show()