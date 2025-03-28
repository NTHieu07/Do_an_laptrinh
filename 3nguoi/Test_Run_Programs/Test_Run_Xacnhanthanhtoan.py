from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Khach_hang.thanhtoan.XacnhanthanhtoanExt import XacnhanthanhtoanExt

app = QApplication([])
MainWindow = QMainWindow()
myui = XacnhanthanhtoanExt()
myui.setupUi(MainWindow)
MainWindow.show()
app.exec()