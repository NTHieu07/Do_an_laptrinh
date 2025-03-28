import os

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox, QMainWindow

from Models.Employee import Employee
from libs.JsonFileFactory import JsonFileFactory
from ui.Quanly.QuanLyNhanVien.MainWindow import Ui_MainWindow

# Import JsonFileFactory



class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dataset = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.FILE_PATH = os.path.join(current_dir, "..", "..", "..", "Dataset", "database.json")
        self.nam = os.path.join(current_dir, "..", "..", "..", "images" , "Nhanvien" , "ic_man.png")
        self.nu = os.path.join(current_dir, "..", "..", "..", "images" , "Nhanvien" , "ic_woman.png")
        self.back = os.path.join(current_dir, "..", "..", "..", "images", "back.png")
        self.timkiem = os.path.join(current_dir, "..", "..", "..", "images" , "Nhanvien" , "find.webp")
        self.background = os.path.join(current_dir, "..", "..", "..", "images", "backround.png")
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.readEmployeeFromJson()
        self.MainWindow.closeEvent = self.closeEvent
        self.HomeButton.setIcon(QtGui.QIcon(self.back))
        self.findempbutton.setIcon(QtGui.QIcon(self.timkiem))
        self.label_6.setPixmap(QtGui.QPixmap(self.background))
        self.Setupsingalandslots()
    def show(self):
        self.MainWindow.show()
    def Setupsingalandslots(self):
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.listWidgetEmployee.itemSelectionChanged.connect(self.processItemSelectionChanged)
        self.pushButtonDelete.clicked.connect(self.processDelete)
        self.findempbutton.clicked.connect(self.timnhanvien)
        self.hienthibutton.clicked.connect(self.hienthitatca)
        self.HomeButton.clicked.connect(self.Home)
    def processNew(self):
        self.lineEditTen.clear()
        self.lineEditId.clear()
        self.lineEditNgaysinh.clear()
        self.lineEditChucvu.clear()
        self.radNu.setChecked(True)
        self.lineEditTen.setFocus()

    def processSave(self):
        name = self.lineEditTen.text().strip()
        emp_id = self.lineEditId.text().strip()
        ngay_sinh = self.lineEditNgaysinh.text().strip()
        chuc_vu = self.lineEditChucvu.text().strip()
        gender = self.radNu.isChecked()

        if not name or not emp_id or not ngay_sinh or not chuc_vu:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin nhân viên!")
            return

        new_emp = Employee(name, emp_id, gender, ngay_sinh, chuc_vu)
        isUpdated = False

        # Cập nhật nhân viên nếu ID đã tồn tại trong self.dataset
        for i, emp in enumerate(self.dataset):
            if emp.id.lower() == emp_id.lower():
                self.dataset[i] = new_emp
                isUpdated = True
                break

        # Nếu không có, thêm mới vào self.dataset
        if not isUpdated:
            self.dataset.append(new_emp)

        # Sau khi cập nhật self.dataset, làm mới giao diện listWidget với toàn bộ dữ liệu
        self.hienthitatca()
        self.writeEmployeeToJson()
        QMessageBox.information(self.MainWindow, "Thông báo", "Nhân viên đã được lưu thành công!")

    def processItemSelectionChanged(self):
        """Khi chọn nhân viên, hiển thị thông tin lên form."""
        current_row = self.listWidgetEmployee.currentRow()
        if current_row < 0:
            return

        item = self.listWidgetEmployee.item(current_row)
        emp = item.data(Qt.ItemDataRole.UserRole)

        self.lineEditTen.setText(emp.ten)
        self.lineEditId.setText(emp.id)
        self.lineEditNgaysinh.setText(emp.ngay_sinh)
        self.lineEditChucvu.setText(emp.chuc_vu)
        self.radNu.setChecked(emp.gioi_tinh)
        self.radNam.setChecked(not emp.gioi_tinh)

    def processDelete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Xác nhận',
            'Bạn có chắc chắn muốn xóa nhân viên đã chọn?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return

        # Xóa nhân viên được đánh dấu trong listWidget và cập nhật self.dataset tương ứng
        indexes_to_delete = []
        for index in range(self.listWidgetEmployee.count()):
            item = self.listWidgetEmployee.item(index)
            if item.checkState() == Qt.CheckState.Checked:
                emp = item.data(Qt.ItemDataRole.UserRole)
                indexes_to_delete.append(emp.id.lower())

        if indexes_to_delete:
            # Lọc lại self.dataset để xóa các nhân viên đã chọn
            self.dataset = [emp for emp in self.dataset if emp.id.lower() not in indexes_to_delete]

        self.processNew()
        self.hienthitatca()
        self.writeEmployeeToJson()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self.MainWindow,
            "Xác nhận",
            "Bạn có muốn tắt cửa sổ không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    # Sử dụng JsonFileFactory để ghi dữ liệu JSON từ self.dataset
    def writeEmployeeToJson(self):
        factory = JsonFileFactory()
        factory.write_data(self.dataset, self.FILE_PATH)

    # Sử dụng JsonFileFactory để đọc dữ liệu JSON và cập nhật self.dataset cũng như listWidget
    def readEmployeeFromJson(self):
        factory = JsonFileFactory()
        self.dataset = factory.read_data(self.FILE_PATH, Employee)
        self.refreshListWidget()

    # Hàm làm mới listWidget từ self.dataset
    def refreshListWidget(self):
        self.listWidgetEmployee.clear()
        for emp in self.dataset:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setText(str(emp))
            item.setCheckState(Qt.CheckState.Unchecked)
            item.setIcon(QIcon(self.nu)
                          if emp.gioi_tinh else QIcon(self.nam))
            self.listWidgetEmployee.addItem(item)

    def timnhanvien(self):
        findnv = self.findemp.text().strip().lower()

        if not findnv:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập tên hoặc ID nhân viên cần tìm!")
            return

        self.listWidgetEmployee.clear()  # Xóa danh sách hiện tại

        for emp in self.dataset:
            if findnv in emp.ten.lower() or findnv in emp.id.lower() or findnv in emp.chuc_vu.lower():
                item = QListWidgetItem()
                item.setData(Qt.ItemDataRole.UserRole, emp)
                item.setText(str(emp))
                item.setCheckState(Qt.CheckState.Unchecked)
                item.setIcon(QIcon(self.nu)
                              if emp.gioi_tinh else QIcon(self.nam))
                self.listWidgetEmployee.addItem(item)
        if self.listWidgetEmployee.count() == 0:
            QMessageBox.information(self.MainWindow, "Kết quả", "Không tìm thấy nhân viên nào!")

    def hienthitatca(self):
        self.refreshListWidget()
    def Home(self):
        self.MainWindow.hide()
        from ui.Quanly.Giaodien.QuanlyExt import QuanlyExt
        # Tạo cửa sổ mới cho giao diện quản lý
        self.quanly_window = QMainWindow()
        self.quanly_ui = QuanlyExt()
        self.quanly_ui.setupUi(self.quanly_window)
        self.quanly_window.show()