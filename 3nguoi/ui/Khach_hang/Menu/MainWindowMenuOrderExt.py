import os

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QPixmap

from Models.Order import Order
from libs.Dataconnector import DataConnector
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QScrollArea, QWidget, QGridLayout, \
    QTableWidgetItem, QHBoxLayout, QMessageBox, QMainWindow
from PyQt6.QtCore import Qt
from ui.Khach_hang.Menu.MainWindowMenuOrder import Ui_MainWindow
from ui.Khach_hang.thanhtoan.ThanhtoanExt import ThanhtoanExt


class MainWindowMenuOrderExt(Ui_MainWindow):
    def __init__(self):
        self.cart_items = {}

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.MainWindow = MainWindow
        self.tableWidget.setColumnWidth(0, 200)
        self.data_connector = DataConnector()
        self.categories = self.data_connector.get_all_categories()
        self.products = self.data_connector.get_all_products()

        self.pushButtonThanhToan.clicked.connect(self.thanh_toan)
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QTableView.SelectionBehavior.SelectRows)  # click item sẽ tô màu dòng item đó
        self.menu()
        self.Quaylaibutton.clicked.connect(self.Home)
        # Xác định thư mục hiện tại của file Python
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Nối đường dẫn đến file icon
        icon_path = os.path.join(current_dir, "..", "..", "..", "images", "skibidi.png")
        # Load icon
        icon = QtGui.QIcon(icon_path)
        self.MainWindow.setWindowIcon(icon)

    def menu(self):
        # Xóa các tab hiện có (nếu có)
        self.tabWidget.clear()

        # Duyệt qua từng danh mục
        for category in self.categories:
            category_name = category.name
            products_in_category = category.products


            # Tạo tab mới cho danh mục
            tab = QWidget()
            tab_layout = QVBoxLayout()

            # Tạo vùng cuộn cho sản phẩm
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_content = QWidget()
            scroll_layout = QVBoxLayout(scroll_content)

            # Tạo lưới để hiển thị sản phẩm
            grid_layout = QGridLayout()
            row, col = 0, 0

            # Duyệt qua các sản phẩm trong self.products (chứa product.name, product.size, product.price, v.v.)
            for product in self.products:
                # Tạo chuỗi "Tên + size", ví dụ: "Cà Phê Sữa 700"
                product_full_name = product.name.strip() + " " + product.size.strip()

                # Kiểm tra xem product_full_name có khớp với phần trước dấu ":" của bất kỳ chuỗi nào trong category.products
                found = False
                for p in products_in_category:
                    left_part = p.split(":")[0].strip()  # => "Cà Phê Sữa 700"
                    if product_full_name.lower() == left_part.lower():
                        found = True
                        break

                if not found:
                    # Sản phẩm này không thuộc danh mục hiện tại
                    continue

                # Tạo khung cho mỗi sản phẩm
                frame = QFrame()
                frame.setMaximumSize(150, 200)
                frame.setStyleSheet("background-color: rgb(4, 140, 252);"
                                    "border-raidus: 10px")
                frame.setFrameShape(QFrame.Shape.Panel)
                frame.setFrameShadow(QFrame.Shadow.Raised)
                frame.setLineWidth(3)

                # Tạo bố cục dọc cho khung
                frame_layout = QVBoxLayout()

                # Thêm ảnh sản phẩm
                image_label = QLabel()

                filename = os.path.basename(product.image_path)
                current_dir = os.path.dirname(os.path.abspath(__file__))
                # Sau đó xây dựng đường dẫn tương đối cho ảnh:
                image_path = os.path.join(current_dir, "..", "..", "..", "images", "DoUong", filename)
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
                    image_label.setPixmap(pixmap)
                else:
                    image_label.setText("Ảnh không tải được")
                image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                frame_layout.addWidget(image_label)

                # Thêm tên sản phẩm
                label_name = QLabel(product.name)
                label_name.setMinimumSize(0, 20)
                label_name.setStyleSheet("background-color: rgb(208, 255, 222);"
                                         "color: rgb(0, 0, 0);"
                                         "border-radius: 3px")
                label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
                frame_layout.addWidget(label_name)

                # Thêm giá sản phẩm
                label_price = QLabel(f"{product.price:,} VNĐ")
                label_price.setMinimumSize(0, 20)
                label_price.setStyleSheet("background-color: rgb(208, 255, 222);"
                                          "color: rgb(0, 0, 0);"
                                          "border-radius: 3px")
                label_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
                frame_layout.addWidget(label_price)

                # Thêm nút "Thêm"
                add_button = QPushButton("Thêm")
                add_button.clicked.connect(lambda checked, p=product: self.add_to_cart(p))
                add_button.setStyleSheet("color: rgb(0, 0, 255);"
                                         "background-color: rgb(0, 255, 255)")
                frame_layout.addWidget(add_button)

                # Đặt bố cục cho khung
                frame.setLayout(frame_layout)

                # Thêm khung vào lưới
                grid_layout.addWidget(frame, row, col)
                col += 1
                if col > 2:  # Chuyển sang hàng mới sau 3 cột
                    col = 0
                    row += 1

            # Thêm lưới vào nội dung vùng cuộn
            scroll_layout.addLayout(grid_layout)
            scroll_area.setWidget(scroll_content)
            tab_layout.addWidget(scroll_area)
            tab.setLayout(tab_layout)

            # Thêm tab vào tabWidget
            self.tabWidget.setStyleSheet("background-color: rgb(179, 229, 252);")
            self.tabWidget.addTab(tab, category_name)

    def add_to_cart(self, product):
        # Tạo key để hiển thị trong bảng = "Tên sản phẩm + size"
        product_key = f"{product.name} {product.size}"
        price = product.price

        # Cập nhật các mục trong giỏ hàng
        if product_key in self.cart_items:
            self.cart_items[product_key][0] += 1  # Tăng số lượng
            self.cart_items[product_key][2] = self.cart_items[product_key][0] * price  # Cập nhật tổng giá
        else:
            # [số_lượng, giá, tổng_giá]
            self.cart_items[product_key] = [1, price, price]

        # Cập nhật bảng giỏ hàng
        self.update_cart_table()

    def update_cart_table(self):
        # Xóa nội dung bảng hiện tại
        self.tableWidget.setRowCount(0)

        # Thêm các mục từ giỏ hàng vào bảng
        total_price = 0
        for row, (product_name, (quantity, price, total)) in enumerate(self.cart_items.items()):
            self.tableWidget.insertRow(row)

            # Tên sản phẩm
            self.tableWidget.setItem(row, 0, QTableWidgetItem(product_name))
            # Giá
            self.tableWidget.setItem(row, 1, QTableWidgetItem(f"{price:,} VNĐ"))

            # Số lượng
            # Tạo widget cho cột "Số Lượng" với nút tăng/giảm
            quantity_widget = QWidget()
            quantity_layout = QHBoxLayout()
            quantity_layout.setContentsMargins(0, 0, 0, 0)

            # Nút giảm số lượng
            decrease_button = QPushButton("-")
            decrease_button.setFixedSize(20, 20)
            decrease_button.clicked.connect(lambda checked, pn=product_name: self.decrease_quantity(pn))
            quantity_layout.addWidget(decrease_button)

            # Nhãn hiển thị số lượng
            quantity_label = QLabel(str(quantity))
            quantity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            quantity_layout.addWidget(quantity_label)

            # Nút tăng số lượng
            increase_button = QPushButton("+")
            increase_button.setFixedSize(20, 20)
            increase_button.clicked.connect(lambda checked, pn=product_name: self.increase_quantity(pn))
            quantity_layout.addWidget(increase_button)

            quantity_widget.setLayout(quantity_layout)
            self.tableWidget.setCellWidget(row, 2, quantity_widget)
            # Tổng giá
            self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total:,} VNĐ"))

            total_price += total

        # Cập nhật tổng tiền
        self.labelTongTien.setText(f"{total_price:,} VNĐ")

    def increase_quantity(self, product_name):
        if product_name in self.cart_items:
            self.cart_items[product_name][0] += 1
            price = self.cart_items[product_name][1]
            self.cart_items[product_name][2] = self.cart_items[product_name][0] * price
            self.update_cart_table()

    def decrease_quantity(self, product_name):
        if product_name in self.cart_items:
            self.cart_items[product_name][0] -= 1
            if self.cart_items[product_name][0] <= 0:
                del self.cart_items[product_name]
            else:
                price = self.cart_items[product_name][1]
                self.cart_items[product_name][2] = self.cart_items[product_name][0] * price
            self.update_cart_table()

    def thanh_toan(self):
        ten_kh = self.lineEditTenKH.text()
        sdt = self.lineEditSoDienThoai.text()
        if ten_kh == "" or sdt == "":
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Tên và sđt không được để trống")
            self.msg.exec()
        else:
            products_list = []
            for product_name, (quantity, price, total) in self.cart_items.items():
                for i in range(quantity):
                    products_list.append(f"{product_name} : {price}")
            total_price = sum(item[2] for item in self.cart_items.values())
            # Tạo đối tượng Order với thông tin khách hàng và giỏ hàng
            order = Order(name=ten_kh, sdt=sdt, products=products_list, totalprice=total_price)
            # Lấy danh sách đơn hàng hiện có, thêm đơn hàng mới, sau đó ghi lại vào file order.json
            orders = self.data_connector.get_all_orders()
            orders.append(order)
            self.data_connector.json_factory.write_data(orders, self.data_connector.order_file)
            # Xóa giỏ hàng sau khi thanh toán
            self.cart_items = {}
            self.update_cart_table()
            self.MainWindow.close()
            # Tạo cửa sổ mới cho giao diện thanh toán
            self.thanhtoan_window = QMainWindow()
            self.thanhtoan_ui = ThanhtoanExt()
            self.thanhtoan_ui.setupUi(self.thanhtoan_window)
            self.thanhtoan_window.show()

    def showWindow(self):
        self.MainWindow.show()
    def Home(self):
        self.MainWindow.hide()

        from ui.Login.LoginExt import LoginExt
        self.modau_window = QMainWindow()
        self.modau_ui = LoginExt()
        self.modau_ui.setupUi(self.modau_window)
        self.modau_window.show()