from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Quanly.LichSuHoaDon.LichsuhoadonExt import LichsuhoadonExt

app = QApplication([])
MainWindow = QMainWindow()
myui = LichsuhoadonExt()
myui.setupUi(MainWindow)
MainWindow.show()
app.exec()