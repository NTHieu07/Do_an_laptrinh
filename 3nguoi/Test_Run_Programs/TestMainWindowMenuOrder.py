
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Khach_hang.Menu.MainWindowMenuOrderExt import MainWindowMenuOrderExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowMenuOrderExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()