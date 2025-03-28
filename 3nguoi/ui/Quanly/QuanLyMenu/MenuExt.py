import os

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox, QFileDialog
from Models.Category import Category
from libs.Dataconnector import DataConnector
from ui.Quanly.QuanLyMenu.Menu import Ui_MainWindow

class MenuExt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_signals()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.back = os.path.join(current_dir, "..", "..", "..", "images" , "back.png")
        self.background = os.path.join(current_dir, "..", "..", "..", "images", "backround.png")
        self.label_3.setPixmap(QtGui.QPixmap(self.background))
        self.HomeButton.setIcon(QtGui.QIcon(self.back))
        # Kết nối với DataConnector để đọc/ghi dữ liệu
        self.data_connector = DataConnector()

        # Khởi tạo danh sách sản phẩm và danh mục
        self.danh_sach_san_pham = []
        self.danh_sach_danh_muc = []

        self.tai_du_lieu_tu_json()

    def setup_signals(self):
        self.pushButton_ThemSP.clicked.connect(self.them_san_pham)
        self.pushButton_ChinhSua.clicked.connect(self.chinh_sua_san_pham)
        self.pushButton_Xoa.clicked.connect(self.xoa_san_pham)
        self.comboBox_LocSanPhamTheoDanhMuc.currentIndexChanged.connect(self.loc_san_pham_theo_danh_muc)
        self.tableWidget.itemSelectionChanged.connect(self.chitietsanpham)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectionBehavior.SelectRows)  # click item sẽ tô màu dòng item đó
        self.HomeButton.clicked.connect(self.Home)

    def get_value(self, obj, key):
        """Trả về giá trị của obj[key] nếu dict, hoặc getattr(obj, key) nếu đối tượng."""
        if isinstance(obj, dict):
            return obj.get(key, "")
        else:
            return getattr(obj, key, "")

    def tai_du_lieu_tu_json(self):
        try:
            # Đọc danh sách sản phẩm và danh mục
            self.danh_sach_san_pham = self.data_connector.get_all_products()
            print("Đã đọc danh sách sản phẩm:", self.danh_sach_san_pham)

            self.danh_sach_danh_muc = self.data_connector.get_all_categories()
            print("Đã đọc danh sách danh mục:", self.danh_sach_danh_muc)

            self.cap_nhat_bang_san_pham()
            self.cap_nhat_combobox_danh_muc()
        except Exception as e:
            print("Lỗi khi đọc dữ liệu từ file JSON:", e)
            QMessageBox.warning(self, "Lỗi", f"Không thể đọc dữ liệu: {e}")

    def cap_nhat_bang_san_pham(self, danh_sach=None):
        if danh_sach is None:
            danh_sach = self.danh_sach_san_pham
            self.filtered_product_list = danh_sach  # Nếu không lọc, gán danh sách gốc
        self.tableWidget.setRowCount(0)
        for sp in danh_sach:
            name = self.get_value(sp, "name")
            size = self.get_value(sp, "size")
            price = self.get_value(sp, "price")
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(name) + " " + str(size)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(size)))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(price)))

    def cap_nhat_combobox_danh_muc(self):
        self.comboBox_LocSanPhamTheoDanhMuc.clear()
        self.comboBox_LocSanPhamTheoDanhMuc.addItem("Tất cả")
        for dm in self.danh_sach_danh_muc:
            self.comboBox_LoaiDoUong.addItem(dm.name)  # Nếu comboBox_LoaiDoUong được sử dụng cho danh mục
            self.comboBox_LocSanPhamTheoDanhMuc.addItem(dm.name)

    def format_product_string(self, name, size, price):
        """
        Định dạng chuỗi sản phẩm: "Tên sản phẩm Size : Giá"
        Ví dụ: "Nước ép dâu 700 : 10000"
        """
        return f"{name} {size} : {price}"

    def luu_du_lieu_vao_json(self):
        try:
            self.data_connector.save_all_products(self.danh_sach_san_pham)
            self.data_connector.save_all_categories(self.danh_sach_danh_muc)
        except Exception as e:
            print("Lỗi khi lưu dữ liệu:", e)
            QMessageBox.warning(self, "Lỗi", f"Không thể lưu dữ liệu: {e}")

    # -------------------------------------------------------
    #   HÀM TÌM HOẶC TẠO DANH MỤC
    # -------------------------------------------------------
    def tim_hoac_tao_danh_muc(self, ten_danh_muc):
        for cat in self.danh_sach_danh_muc:
            if cat.name.lower().strip() == ten_danh_muc.lower().strip():
                return cat
        new_cat = Category(ten_danh_muc, [])
        self.danh_sach_danh_muc.append(new_cat)
        return new_cat

    # -------------------------------------------------------
    #   THÊM SẢN PHẨM
    # -------------------------------------------------------
    def them_san_pham(self):
        size_san_pham = self.comboBox_SizeDoUong.currentText()
        ten_san_pham = self.lineEditNhapTenSanPham.text()
        gia_san_pham = self.lineEditGia.text()
        danh_muc = self.comboBox_LoaiDoUong.currentText()

        # Hỏi người dùng có muốn thêm ảnh hay không
        ans = QMessageBox.question(
            self,
            'Xác nhận thêm ảnh',
            'Bạn có muốn thêm ảnh cho đồ uống?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if ans == QMessageBox.StandardButton.Yes:
            pic, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        else:
            pic = ""

        if not ten_san_pham or not gia_san_pham or not danh_muc:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ thông tin sản phẩm!")
            return

        new_product = {
            "name": ten_san_pham,
            "size": size_san_pham,
            "price": int(gia_san_pham),
            "danh_muc": danh_muc,
            "image_path": pic
        }
        self.danh_sach_san_pham.append(new_product)
        self.cap_nhat_bang_san_pham()

        product_str = self.format_product_string(ten_san_pham, size_san_pham, gia_san_pham)
        cat = self.tim_hoac_tao_danh_muc(danh_muc)
        cat.products.append(product_str)

        self.luu_du_lieu_vao_json()

        # Reset form
        self.comboBox_SizeDoUong.setCurrentIndex(0)
        self.lineEditNhapTenSanPham.clear()
        self.lineEditGia.clear()
        self.comboBox_LoaiDoUong.setCurrentIndex(0)

    # -------------------------------------------------------
    #   CHỈNH SỬA SẢN PHẨM (VỚI XỬ LÝ DANH MỤC)
    # -------------------------------------------------------
    def chinh_sua_san_pham(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một sản phẩm để chỉnh sửa!")
            return

        # Lấy thông tin sản phẩm cũ
        old_product = self.danh_sach_san_pham[selected_row]
        old_category = self.get_value(old_product, "danh_muc")
        old_name = self.get_value(old_product, "name")
        old_size = self.get_value(old_product, "size")
        old_price = self.get_value(old_product, "price")
        old_product_str = self.format_product_string(old_name, old_size, old_price)

        size_san_pham = self.comboBox_SizeDoUong.currentText()
        ten_san_pham = self.lineEditNhapTenSanPham.text()
        gia_san_pham = self.lineEditGia.text()
        new_category = self.comboBox_LoaiDoUong.currentText()

        # Hỏi người dùng có muốn chỉnh sửa ảnh hay không
        ans = QMessageBox.question(
            self,
            'Xác nhận chỉnh sửa ảnh',
            'Bạn có muốn chỉnh sửa ảnh cho đồ uống?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if ans == QMessageBox.StandardButton.Yes:
            pic, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", os.path.expanduser("~"),
                                                 "Image Files (*.png *.jpg *.jpeg *.bmp)")
            if pic == "": #Trong lúc tìm ảnh mà out thì giữ lại ảnh cũ, nếu ảnh cũ không có thì coi như trống
                if isinstance(old_product, dict):
                    pic = old_product.get("image_path", "")
                else:
                    pic = getattr(old_product, "image_path", "")
        else:
            # Nếu không muốn chỉnh sửa ảnh, giữ nguyên ảnh cũ (nếu có)
            if isinstance(old_product, dict):
                pic = old_product.get("image_path", "")
            else:
                pic = getattr(old_product, "image_path", "")

        if not ten_san_pham or not gia_san_pham or not new_category:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ thông tin sản phẩm!")
            return

        updated_product = {
            "name": ten_san_pham,
            "size": size_san_pham,
            "price": int(gia_san_pham),
            "danh_muc": new_category,
            "image_path": pic
        }
        self.danh_sach_san_pham[selected_row] = updated_product
        self.cap_nhat_bang_san_pham()

        new_product_str = self.format_product_string(ten_san_pham, size_san_pham, gia_san_pham)

        # Loại bỏ sản phẩm cũ khỏi danh mục cũ
        for cat in self.danh_sach_danh_muc:
            if cat.name.lower().strip() == old_category.lower().strip():
                for s in cat.products:
                    if old_name.lower().strip() in s.lower() and old_size.lower().strip() in s.lower():
                        cat.products.remove(s)
                        break
                break

        cat_new = self.tim_hoac_tao_danh_muc(new_category)
        cat_new.products.append(new_product_str)

        self.luu_du_lieu_vao_json()

        # Reset form
        self.comboBox_SizeDoUong.setCurrentIndex(0)
        self.lineEditNhapTenSanPham.clear()
        self.lineEditGia.clear()
        self.comboBox_LoaiDoUong.setCurrentIndex(0)

    # -------------------------------------------------------
    #   XÓA SẢN PHẨM
    # -------------------------------------------------------
    def xoa_san_pham(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một sản phẩm để xóa!")
            return

        old_product = self.danh_sach_san_pham[selected_row]
        old_category = self.get_value(old_product, "danh_muc")
        old_product_str = self.format_product_string(
            self.get_value(old_product, "name"),
            self.get_value(old_product, "size"),
            self.get_value(old_product, "price")
        )

        self.danh_sach_san_pham.pop(selected_row)
        self.cap_nhat_bang_san_pham()

        for cat in self.danh_sach_danh_muc:
            if cat.name.lower().strip() == old_category.lower().strip():
                if old_product_str in cat.products:
                    cat.products.remove(old_product_str)
                break

        self.luu_du_lieu_vao_json()

    # -------------------------------------------------------
    #   LỌC SẢN PHẨM THEO DANH MỤC
    # -------------------------------------------------------
    def loc_san_pham_theo_danh_muc(self):
        selected_category = self.comboBox_LocSanPhamTheoDanhMuc.currentText()
        if selected_category == "Tất cả":
            self.filtered_product_list = self.danh_sach_san_pham
        else:
            self.filtered_product_list = []
            for sp in self.danh_sach_san_pham:
                dm = self.get_value(sp, "danh_muc").strip().lower()
                if dm == selected_category.lower():
                    self.filtered_product_list.append(sp)
        self.cap_nhat_bang_san_pham(self.filtered_product_list)

    # -------------------------------------------------------
    #   HIỂN THỊ CHI TIẾT SẢN PHẨM
    # -------------------------------------------------------
    def chitietsanpham(self):
        index = self.tableWidget.currentRow()
        if index < 0:
            return

        product = self.filtered_product_list[index]
        self.lineEditNhapTenSanPham.setText(str(self.get_value(product, "name")))
        self.lineEditGia.setText(str(self.get_value(product, "price")))

        size = str(self.get_value(product, "size")).strip().lower()
        if "700" in size:
            self.comboBox_SizeDoUong.setCurrentIndex(0)
        else:
            self.comboBox_SizeDoUong.setCurrentIndex(1)

        current_category = str(self.get_value(product, "danh_muc")).strip()
        idx = -1
        for i in range(self.comboBox_LoaiDoUong.count()):
            item_text = self.comboBox_LoaiDoUong.itemText(i).strip()
            if item_text.lower() == current_category.lower():
                idx = i
                break
        if idx >= 0:
            self.comboBox_LoaiDoUong.setCurrentIndex(idx)
        else:
            self.comboBox_LoaiDoUong.setCurrentIndex(0)
    def Home(self):
        self.close()
        from ui.Quanly.Giaodien.QuanlyExt import QuanlyExt
        # Tạo cửa sổ mới cho giao diện quản lý
        self.quanly_window = QMainWindow()
        self.quanly_ui = QuanlyExt()
        self.quanly_ui.setupUi(self.quanly_window)
        self.quanly_window.show()