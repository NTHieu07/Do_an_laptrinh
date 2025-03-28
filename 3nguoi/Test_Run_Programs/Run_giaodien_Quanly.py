from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Quanly.Giaodien.QuanlyExt import QuanlyExt

app = QApplication([])
MainWindow = QMainWindow()
myui = QuanlyExt()
myui.setupUi(MainWindow)
MainWindow.show()
app.exec()