from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Quanly.ThongKeWindow.ThongkeExt import ThongkeExt

app = QApplication([])
MainWindow = QMainWindow()
myui = ThongkeExt()
myui.setupUi(MainWindow)
MainWindow.show()
app.exec()