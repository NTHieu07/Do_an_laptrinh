from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Quanly.QuanLyNhanVien.MainWindowEx import MainWindowEx

app=QApplication([])
MainWindow = QMainWindow()
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()