
from PyQt6.QtWidgets import QMainWindow, QApplication

from ui.Khach_hang.thanhtoan.ThanhtoanExt import ThanhtoanExt

app = QApplication([])
MainWindow = QMainWindow()
myui = ThanhtoanExt()
myui.setupUi(MainWindow)
MainWindow.show()
app.exec()